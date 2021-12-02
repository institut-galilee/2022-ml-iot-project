from network.access_point import AccessPoint
import subprocess
from threading import Thread
import time
import sys
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import FileSystemEventHandler
from diff_match_patch import diff_match_patch
from collections import namedtuple


logging.basicConfig(level=logging.INFO,
                    format='[WifiAccessPoint] %(asctime)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


NewConnexionEvent = namedtuple('NewConnexionEvent', ['macAdd', 'ipAdd', 'deviceName', 'clientId'])


class DiffHandler(FileSystemEventHandler):
    def __init__(self, netManager, to_watch):
        self.netManager = netManager
        self.differ = diff_match_patch()
        self.to_watch = to_watch
        with open(self.to_watch) as f:
            self.last_contents = f.read()

    def on_modified(self, event):
        if event.src_path == self.to_watch:
            with open(self.to_watch) as f:
                new_contents = f.read()
            patch = self.differ.patch_make(self.last_contents, new_contents)
            patch_text = self.differ.patch_toText(patch)
            logging.info(patch_text)
            self.last_contents = new_contents

        # process the modifications
        # TODO better handling of the different scenarios
        # for now, only one scenario is handled,
        # i.e., when the phone connects for the first time and a newline is created
        # e.g., 1638115769 e0:aa:96:37:ea:24 10.42.0.100 Galaxy-J5 01:e0:aa:96:37:ea:24
        try:
            print(patch[0].__dict__)

            newline = patch[0].diffs[0][1]
            elems = newline.split()
            for elem in elems:
                print(elem)

            # In the considered scenario, we should get 5 elements when we split the newline
            # - Time of lease expiry
            # - mac address
            # - assigned IP address
            # - device name
            # - Client-ID
            if len(elems) == 5:
                # signal that a new device is connected to the access point
                logging.info('NewConnexionEvent')
                event = NewConnexionEvent(elems[1], elems[2], elems[3], elems[4])
                self.netManager.notifyObservers(event)
        except IndexError:
            logging.warning('trying to access to empty patch ... TODO: find-out why this buggy behavior')


class WiFiAccessPoint(AccessPoint):
    name = "toto"
    address = "toto"

    def __init__(self, networkManager):
        self.netManager = networkManager

    def setup(self):
        # system file where new connections to the hotspot are logged
        self.dnsmasq_leases = '/var/lib/misc/dnsmasq.leases'

    def start(self):
        # TODO
        # `Hotspot` is the connection id.
        # It has to be retreived in the `setup()` from
        # /etc/NetworkManager/system-connections/Hotspot (require sudo)
        # using the two following commands
        # > UUID=$(grep uuid /etc/NetworkManager/system-connections/Hotspot | cut -d= -f2)
        # > nmcli con up uuid $UUID
        res = subprocess.check_output(
            f'nmcli con up Hotspot',
            shell=True
        ).decode('utf-8')

        # TODO
        # handle possible errors here

        if res.startswith('Connection successfully activated'):
            print('WiFi Access Point successfully activated')

    def stop(self):
        res = subprocess.check_output(
            f'nmcli con down Hotspot',
            shell=True
        ).decode('utf-8')

        # TODO
        # handle possible errors here

        if res.startswith('Connection \'Hotspot\' successfully deactivated'):
            print('WiFi Access Point successfully deactivated')

    def monitoring(self):
        # path = sys.argv[1] if len(sys.argv) > 1 else '.'
        path = self.dnsmasq_leases
        # logging_handler = LoggingEventHandler()
        diff_handler = DiffHandler(self.netManager, path)

        observer = Observer()
        # observer.schedule(logging_handler, path, recursive=True)
        observer.schedule(diff_handler, path, recursive=False)
        observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()

    def monitorIncomingConnections(self):
        t = Thread(target=self.monitoring, daemon=True)
        t.start()
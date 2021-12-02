from network.wifi_access_point import WiFiAccessPoint
from collections import namedtuple
import logging


logging.basicConfig(level=logging.INFO,
                    format='[NetworkManagerContext] %(asctime)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


# TODO move to main or controller program
Config = namedtuple('Config', ['ap'])
config = Config('WIFI')


class NetworkManagerContext:
    def __init__(self, config):
        self.observerCollection = []
        if config.ap == 'WIFI':
            self.accessPoint = WiFiAccessPoint(self)
        elif config.ap == 'BLUETOOTH':
            raise NotImplementedError
        else:
            raise NotImplementedError
        self.accessPoint.setup()

    def start(self):
        self.accessPoint.start()

    def monitorIncomingConnections(self):
        self.accessPoint.monitorIncomingConnections()

    def stop(self):
        self.accessPoint.stop()

    def registerObserver(self, observer):
        observerCollection.append(observer)

    def notifyObservers(self, event):
        logging.info(event)
        for observer in self.observerCollection:
            observer.notify(event)
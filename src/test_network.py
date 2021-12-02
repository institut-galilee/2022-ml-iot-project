from network.wifi_access_point import WiFiAccessPoint
from network.network_manager import NetworkManagerContext
import time
from collections import namedtuple


def main():
    Config = namedtuple('Config', ['ap'])
    config = Config('WIFI')
    netManager = NetworkManagerContext(config)
    netManager.start()
    print("Monitoring incoming connections ...")
    netManager.monitorIncomingConnections()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        netManager.stop()


if __name__ == '__main__':
    main()
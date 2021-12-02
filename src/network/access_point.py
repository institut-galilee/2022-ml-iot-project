from abc import ABCMeta, abstractclassmethod


class AccessPoint(metaclass=ABCMeta):
    @property
    @abstractclassmethod
    def address(self) -> str:
        """
        :address returns the address of the access point
        e.g., in the case of WiFi access point, it would be the IP address
        while in the case of Bluetooth master device, it would be the BD_ADDR.
        """
        ...

    @property
    @abstractclassmethod
    def name(self) -> str:
        ...

    @staticmethod
    @abstractclassmethod
    def setup(self):
        """Set the local network parameters up,
        e.g. ssid in the case of WiFi Access Point"""

    def start(self):
        """
        """

    def stop(self):
        """
        """
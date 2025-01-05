import socket
import time

from typing import List
from zeroconf import ServiceBrowser, ServiceListener, Zeroconf

import logging
log = logging.getLogger(__name__)


class DeviceListener(ServiceListener):
    def __init__(self):
        self.devices = {}

    def update_service(self, zc: Zeroconf, type_: str, name: str) -> None:
        # print(f"Service {name} updated")
        info = zc.get_service_info(type_, name)
        self.devices[name] = info

    def remove_service(self, zc: Zeroconf, type_: str, name: str) -> None:
        # print(f"Service {name} removed")
        self.devices.pop(name)

    def add_service(self, zc: Zeroconf, type_: str, name: str) -> None:
        info = zc.get_service_info(type_, name)
        # print(f"Service {name} added, service info: {info}")
        self.devices[name] = info
        # addr = info.addresses[0][0]
        # print(info.type)
        # print(f'info: {addr}')


class BridgeFinder:
    def __init__(self):
        self.zeroconf = Zeroconf()
        self.listener = DeviceListener()
        self.browser = ServiceBrowser(self.zeroconf, "_hue._tcp.local.", self.listener)

    def close(self):
        self.zeroconf.close()

    def get_bridge_server_lists(self) -> List[str]:
        name = [device.server for device in self.listener.devices.values()]
        return name
    
    def get_bridge_addresses(self) -> List[str]:
        return [socket.inet_ntoa(addr) for device in self.listener.devices.values() for addr in device.addresses]


if __name__ == '__main__':
    finder = BridgeFinder()
    time.sleep(3)
    print(finder.get_bridge_server_lists())
    print(finder.get_bridge_addresses())
    try:
        input("Press enter to exit...\n\n")
    finally:
        finder.close()

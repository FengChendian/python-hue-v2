from typing import List
from ..bridge import Bridge
from .zone_get import ZoneGet

import logging
log = logging.getLogger(__name__)


class Zone:
    def __init__(self, bridge: Bridge, zone_id_v2: str):
        self.bridge = bridge
        self.id: str = zone_id_v2

    def _get(self) -> dict:
        return self.bridge.get_zone(self.id)

    def _set(self, room_property_name: str, property_value: dict) -> List[dict]:
        return self.bridge.set_zone(self.id, room_property_name, property_value)
    
    def get(self):
        return ZoneGet(self._get())
from typing import List
from ..bridge import Bridge
from .room_get import RoomGet

import logging
log = logging.getLogger(__name__)


class Room:
    def __init__(self, bridge: Bridge, room_id_v2: str):
        self.bridge = bridge
        self.id: str = room_id_v2

    def _get(self) -> dict:
        return self.bridge.get_room(self.id)

    def _set(self, room_property_name: str, property_value: dict) -> List[dict]:
        return self.bridge.set_room(self.id, room_property_name, property_value)
    
    def get(self):
        return RoomGet(self._get())
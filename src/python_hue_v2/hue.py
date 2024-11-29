import time

from .room import Room
from .bridge import Bridge
from .light import Light
from .scene import Scene, ScenePost
from .grouped_light import GroupedLight
from typing import List, Union, Optional
from .zone.zone import Zone

import logging
log = logging.getLogger(__name__)



class Hue:
    def __init__(self, ip_address: str, hue_application_key: Optional[str] = None):
        self.bridge = Bridge(ip_address=ip_address, hue_application_key=hue_application_key)

    @property
    def lights(self) -> List[Light]:
        return [Light(self.bridge, light_data['id']) for light_data in self.bridge.get_lights()]

    @property
    def scenes(self) -> List[Scene]:
        return [Scene(self.bridge, scene_data['id']) for scene_data in self.bridge.get_scenes()]

    @property
    def grouped_lights(self) -> List[GroupedLight]:
        return [
            GroupedLight(self.bridge, grouped_light_data['id'])
            for grouped_light_data in self.bridge.get_grouped_lights()
        ]

    @property
    def rooms(self) -> List[Room]:
        return [Room(bridge=self.bridge, room_id_v2=room_data['id']) for room_data in self.bridge.get_rooms()]

    @property
    def zones(self) -> List[Zone]:
        return [Zone(bridge=self.bridge, zone_id_v2=zone_data['id']) for zone_data in self.bridge.get_zones()]

    def create_scene(self, properties: Union[dict, ScenePost]) -> list:
        if type(properties) is dict:
            return self.bridge.create_scene(properties)
        elif isinstance(properties, ScenePost):
            return self.bridge.create_scene(properties.data_dict)
        else:
            raise TypeError("Properties must be ScenePost or dict")

    def delete_scene(self, scene_id):
        self.bridge.delete_scene(scene_id=scene_id)

import time

from .bridge import Bridge
from .light import Light
from .scene import Scene
from .grouped_light import GroupedLight
from typing import List


class Hue:
    def __init__(self, ip_address: str, hue_application_key: str):
        self.bridge = Bridge('ecb5fa8549cd.local', '7K-IbBzEV3wZoXkTlSh6HyLTALLFsYrxCjIcW1o9')

    @property
    def lights(self) -> List[Light]:
        return [Light(self.bridge, light_data['id']) for light_data in self.bridge.get_lights()]

    @property
    def scenes(self) -> List[Scene]:
        return [Scene(self.bridge, scene_data['id']) for scene_data in self.bridge.get_scenes()]

    @property
    def grouped_lights(self) -> List[GroupedLight]:
        return [GroupedLight(self.bridge, grouped_light_data['id']) for grouped_light_data in
                self.bridge.get_grouped_lights()]


if __name__ == '__main__':
    hue = Hue('ecb5fa8549cd.local', '7K-IbBzEV3wZoXkTlSh6HyLTALLFsYrxCjIcW1o9')
    scenes = hue.scenes
    for scene in scenes:
        print(scene.data_dict)
    scenes[2].recall(action='static')
    print()
    time.sleep(1)
    grouped_lights = hue.grouped_lights
    grouped_lights[0].on = False
    # hue.lights[0].on = False

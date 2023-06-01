from python_hue_v2.bridge import Bridge
from python_hue_v2.light import Light
from python_hue_v2.scene import Scene
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


if __name__ == '__main__':
    hue = Hue('ecb5fa8549cd.local', '7K-IbBzEV3wZoXkTlSh6HyLTALLFsYrxCjIcW1o9')
    # hue.get_device()
    print()
    hue.lights[0].on = False

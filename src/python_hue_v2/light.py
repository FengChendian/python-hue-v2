from typing import List

from .bridge import Bridge

import logging

log = logging.getLogger(__name__)


class Light:
    def __init__(self, bridge: Bridge, light_id_v2: str):
        self.bridge = bridge
        self.light_id: str = light_id_v2

    def _get(self) -> dict:
        return self.bridge.get_light(self.light_id)

    def _set(self, light_property_name: str, property_value: dict) -> dict:
        return self.bridge.set_light(self.light_id, light_property_name, property_value)

    @property
    def data_dict(self) -> dict:
        return self._get()

    @property
    def on(self) -> bool:
        data = self._get()
        return data['on']['on']

    @on.setter
    def on(self, value: bool):
        self._set('on', {'on': value})

    @property
    def brightness(self) -> float:
        return self._get()['dimming']['brightness']

    @brightness.setter
    def brightness(self, value: float):
        self._set('dimming', {'brightness': value})

    @property
    def color_xy(self) -> dict:
        return self._get()['color']['xy']

    @color_xy.setter
    def color_xy(self, value: dict):
        self._set('color', {'xy': value})

    @property
    def metadata(self) -> dict:
        return self._get()['metadata']

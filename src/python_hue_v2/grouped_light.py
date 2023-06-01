from .bridge import Bridge


class GroupedLight:
    def __init__(self, bridge: Bridge, grouped_light_id: str):
        self.bridge = bridge
        self.grouped_light_id: str = grouped_light_id

    def _get(self):
        return self.bridge.get_grouped_light(self.grouped_light_id)

    def _set(self, property_name: str, property_value: dict) -> dict:
        return self.bridge.set_grouped_light_service(self.grouped_light_id, property_name, property_value)

    @property
    def on(self) -> bool:
        return self._get()['on']['on']

    @on.setter
    def on(self, value: bool):
        self._set('on', {'on': value})

    @property
    def type(self) -> str:
        return self._get()['type']

    @property
    def brightness(self) -> float:
        return self._get()['dimming']['brightness']

    @brightness.setter
    def brightness(self, value: float):
        self._set('dimming', {'brightness': value})

from .bridge import Bridge
import logging
log = logging.getLogger(__name__)


class Owner:
    """ Owner data class for the grouped light owner property """
    def __init__(self, data: dict):
        self._rid: str = data['rid']
        self._rtype: str = data['rtype']

    @property
    def rid(self) -> str:
        return self._rid

    @property
    def rtype(self) -> str:
        return self._rtype


class GroupedLight:
    """API to manage grouped light service, just one group
    Only supports HTTP PUT and GET method.
    """

    def __init__(self, bridge: Bridge, grouped_light_id: str):
        self.bridge = bridge
        self.grouped_light_id: str = grouped_light_id

    def _get(self):
        return self.bridge.get_grouped_light(self.grouped_light_id)

    def _set(self, properties: dict) -> dict:
        """
        _set is equal to HTTP PUT
        :param properties: it is a dict, including type, on, dimming, color_temperature,etc. Please refer to
        https://developers.meethue.com/develop/hue-api-v2/api-reference/#resource_grouped_light__id__put
        :return: Response data, ResourceIdentifierPut, should be a dict for one id, not list
        """
        return self.bridge.set_grouped_light_service(self.grouped_light_id, properties)

    @property
    def data_dict(self) -> dict:
        return self._get()

    @property
    def on(self) -> bool:
        return self._get()['on']['on']

    @on.setter
    def on(self, value: bool):
        self._set({'on': {'on': value}})

    def set_state(self, on: bool, brightness: float = None, duration_ms: int = None):
        """
        Set the state of the grouped light
        :param on: Boolean value to change the state of the grouped light
        :param brightness: Group light brightness value
        :param duration_ms: duration in dynamics
        """
        properties = {'on': {'on': on}}
        if duration_ms:
            properties['dynamics'] = {'duration': duration_ms}
        if brightness:
            properties['dimming'] = {'brightness': brightness}
        self._set(properties)

    @property
    def type(self) -> str:
        return self._get()['type']

    @property
    def brightness(self) -> float:
        return self._get()['dimming']['brightness']

    @brightness.setter
    def brightness(self, value: float):
        self._set({'dimming': {'brightness': value}})

    @property
    def owner(self) -> Owner:
        return Owner(self.data_dict['owner'])

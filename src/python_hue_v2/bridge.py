import json

import requests
import urllib3
from typing import List, Union


class Bridge:
    def __init__(self, ip_address: str, hue_application_key: str):
        self.ip_address = ip_address
        self.hue_application_key = hue_application_key
        self.hue_application_key_str = 'hue-application-key'
        # url
        self.base_url = f'https://{self.ip_address}/clip/v2/resource'

        self._light_category = 'light'
        self._scene_category = 'scene'
        self._room_category = 'room'
        self._zone_category = 'zone'
        self._bridge_home_category = 'bridge_home'
        self._grouped_light_category = 'grouped_light'
        self._device_category = 'device'
        self._bridge_category = 'bridge'

        self.device_list: list = []
        # requests.Request.
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    @staticmethod
    def _get_response_error(r_json: dict):
        return r_json['errors']

    @staticmethod
    def _get_response_data(r_json: dict) -> list:
        return r_json['data']

    @staticmethod
    def _convert_to_data(res: dict) -> List[dict]:
        if res['errors']:
            raise ConnectionError(res['errors'])
        else:
            return res['data']

    def _get_by_id(self, category: str, item_id: str) -> dict:
        url = f'{self.base_url}/{category}/{item_id}'
        res = requests.get(url, headers={self.hue_application_key_str: self.hue_application_key}, verify=False).json()
        return self._convert_to_data(res)[0]

    def _get(self, category: str) -> List[dict]:
        url = f'{self.base_url}/{category}'
        res = requests.get(url, headers={self.hue_application_key_str: self.hue_application_key}, verify=False).json()
        return self._convert_to_data(res)

    def _put_by_id(self, category: str, item_id: str, properties: dict) -> dict:
        url = f'{self.base_url}/{category}/{item_id}'
        res = requests.put(url, data=json.dumps(properties),
                           headers={self.hue_application_key_str: self.hue_application_key},
                           verify=False).json()
        return self._convert_to_data(res)[0]

    def _post(self, category: str, properties: dict) -> list:
        url = f'{self.base_url}/{category}'
        res = requests.post(url, data=json.dumps(properties),
                            headers={self.hue_application_key_str: self.hue_application_key},
                            verify=False).json()
        return self._convert_to_data(res)

    def _delete_by_id(self, category: str, item_id: str) -> list:
        url = f'{self.base_url}/{category}/{item_id}'
        res = requests.delete(url, headers={self.hue_application_key_str: self.hue_application_key},
                              verify=False).json()
        return self._convert_to_data(res)

    def get_light(self, light_id: str) -> dict:
        return self._get_by_id(self._light_category, light_id)

    def get_lights(self) -> List[dict]:
        """
        Get all lights info in bridge
        :return:
        """
        return self._get(self._light_category)

    def set_light(self, light_id_v2, light_property, key_value: dict):
        data = {light_property: key_value}
        return self._put_by_id(self._light_category, light_id_v2, data)

    def get_scenes(self) -> List[dict]:
        return self._get(self._scene_category)

    def get_scene(self, scene_id) -> dict:
        return self._get_by_id(self._scene_category, scene_id)

    def set_scene(self, scene_id, scene_property: str, data: Union[list, dict]):
        return self._put_by_id(self._scene_category, scene_id, {scene_property: data})

    def create_scene(self, properties: dict) -> list:
        return self._post(self._scene_category, properties)

    def delete_scene(self, scene_id: str) -> list:
        return self._delete_by_id(self._scene_category, scene_id)

    def get_rooms(self) -> List[dict]:
        return self._get(self._room_category)

    def get_room(self, room_id: str) -> dict:
        return self._get_by_id(self._room_category, room_id)

    def get_zones(self) -> List[dict]:
        return self._get(self._zone_category)

    def get_zone(self, zone_id: str) -> dict:
        return self._get_by_id(self._zone_category, zone_id)

    def get_devices(self):
        return self._get(self._device_category)

    def get_device(self, device_id: str):
        return self._get_by_id(self._device_category, device_id)

    def get_bridge(self):
        return self._get(self._bridge_category)

    def get_bridge_by_id(self, id_) -> dict:
        """
        Get bridge info by its id
        :param id_: https://developers.meethue.com/develop/hue-api-v2/api-reference/#resource_bridge__id__get
        :return: BridgeGet Info
        """
        return self._get_by_id(self._bridge_category, id_)

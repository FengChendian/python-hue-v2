from typing import List, Optional, Union, Literal
from ..bridge import Bridge
from .action import ActionGet, ActionPost
from .meta_data import MetaData
from .group import Group

import logging
log = logging.getLogger(__name__)

class SceneGet:
    """
    SceneGet Data, ref in https://developers.meethue.com/develop/hue-api-v2/api-reference/#resource_scene_get
    """

    def __init__(self, scene_get_data: dict):
        self._data_dict = scene_get_data
        self._meta_data = MetaData(scene_get_data['metadata'])
        self.actions: list = [ActionGet(action_data) for action_data in self._data_dict['actions']]

    @property
    def data_dict(self) -> dict:
        return self._data_dict

    @property
    def type(self) -> str:
        """
        Get data type
        :return: always get 'scene'
        """
        return self._data_dict['type']

    @property
    def id(self) -> str:
        return self._data_dict['id']

    @property
    def id_v1(self) -> str:
        return self._data_dict['id_v1']

    @property
    def metadata(self) -> MetaData:
        return self._meta_data

    @property
    def group(self) -> dict:
        return self._data_dict['group']

    @property
    def palette(self) -> dict:
        return self._data_dict['palette']

    @property
    def speed(self) -> float:
        return self._data_dict['speed']

    @property
    def auto_dynamic(self) -> bool:
        return self._data_dict['auto_dynamic']


class ScenePut:
    def __init__(self, scene_put_data: dict) -> None:
        self._scene_put_data = scene_put_data

    @property
    def data_dict(self) -> dict:
        return self._scene_put_data


class ScenePost:
    def __init__(self, scene_post_data: dict) -> None:
        self._data_dict: dict = scene_post_data

    @classmethod
    def create_by_parameters(
            cls,
            actions: List[Union[dict, ActionPost]],
            name: str,
            group_rid: str,
            group_rtype: str,
            palette: Optional[dict] = None,
    ):
        if type(actions[0]) is dict:
            action_dicts = actions
        elif isinstance(actions[0], ActionPost):
            action_dicts = [i.data_dict for i in actions]
        else:
            raise TypeError('Actions must be dict or ActionPost')

        post_data = {
            'actions': action_dicts,
            'metadata': {
                'name': name,
            },
            'group': {
                'rid': group_rid,
                'rtype': group_rtype,
            },
        }
        if palette:
            post_data['palette'] = palette
        return cls(post_data)

    @property
    def data_dict(self) -> dict:
        return self._data_dict


class Scene:
    """
    Hue Scene Control Class
    """

    def __init__(self, bridge: Bridge, scene_id_v2: str):
        self.bridge = bridge
        self._scene_id: str = scene_id_v2

    def _get(self) -> dict:
        return self.bridge.get_scene(self._scene_id)

    def _set(self, scene_property_name: str, property_value: Union[list, dict]) -> List[dict]:
        return self.bridge.set_scene(self._scene_id, scene_property_name, property_value)

    def get(self) -> SceneGet:
        return SceneGet(self._get())

    @property
    def data(self) -> SceneGet:
        return SceneGet(self._get())

    @property
    def data_dict(self) -> dict:
        """
        Get raw properties by get
        :return: One SceneGet data in properties. Because 1 id get 1 item.
        https://developers.meethue.com/develop/hue-api-v2/api-reference/#resource_scene__id__get
        """
        return self._get()

    def recall(self, action: Literal['active', 'dynamic_palette', 'static'] = 'active'):
        # {'status': 'active'} is failed
        self._set('recall', {'action': action})

    @property
    def id(self) -> str:
        return self._scene_id

    @property
    def actions(self) -> ActionGet:
        return self.get().actions

    @actions.setter
    def actions(self, action_items: List[dict]):
        self._set('actions', action_items)

    @property
    def meta_data(self) -> MetaData:
        return self.data.metadata

    @property
    def group(self) -> Group:
        return Group(self.data_dict['group'])

    @property
    def status(self) -> dict:
        return self._get()['status']

    @property
    def speed(self) -> float:
        return self._get()['speed']

    @property
    def auto_dynamic(self) -> bool:
        return self._get()['auto_dynamic']

    @property
    def type(self) -> str:
        return self._get()['type']

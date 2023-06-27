from typing import List, Union, Literal
from ..bridge import Bridge
from .action import ActionGet


class SceneGet:
    """
    SceneGet Wrapper in https://developers.meethue.com/develop/hue-api-v2/api-reference/#resource_scene_get
    """

    def __init__(self, scene_get_data: dict):
        self._scene_get_data = scene_get_data
        self.actions: list = [ActionGet(action_data) for action_data in self._scene_get_data['actions']]

    @property
    def type(self) -> str:
        """
        Get data type
        :return: always get 'scene'
        """
        return self._scene_get_data['type']

    @property
    def id(self) -> str:
        return self._scene_get_data['id']

    @property
    def id_v1(self) -> str:
        return self._scene_get_data['id_v1']

    @property
    def metadata(self) -> dict:
        return self._scene_get_data['metadata']

    @property
    def group(self) -> dict:
        return self._scene_get_data['group']

    @property
    def palette(self) -> dict:
        return self._scene_get_data['palette']

    @property
    def speed(self) -> float:
        return self._scene_get_data['speed']

    @property
    def auto_dynamic(self) -> bool:
        return self._scene_get_data['auto_dynamic']


class ScenePut:
    def __init__(self, scene_put_data: dict) -> None:
        self._scene_put_data = scene_put_data

    def to_dict(self) -> dict:
        return self._scene_put_data


class Scene:
    """
    Hue Scene Control Class
    """

    def __init__(self, bridge: Bridge, scene_id_v2: str):
        self.bridge = bridge
        self.scene_id: str = scene_id_v2

    def _get(self) -> dict:
        return self.bridge.get_scene(self.scene_id)

    def _set(self, scene_property_name: str, property_value: Union[list, dict]) -> List[dict]:
        return self.bridge.set_scene(self.scene_id, scene_property_name, property_value)
    
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
        return self.scene_id

    @property
    def actions(self) -> ActionGet:
        return self.get().actions

    @actions.setter
    def actions(self, action_items: List[dict]):
        self._set('actions', action_items)

    @property
    def meta_data(self) -> dict:
        return self._get()['metadata']

    @property
    def group(self) -> dict:
        return self._get()['group']

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
    def type(self) -> dict:
        return self._get()['type']

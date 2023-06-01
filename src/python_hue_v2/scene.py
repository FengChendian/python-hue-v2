from typing import List, Union
from .bridge import Bridge


class SceneGet:
    """
    SceneGet Wrapper in https://developers.meethue.com/develop/hue-api-v2/api-reference/#resource_scene_get
    """
    def __init__(self, scene_get_data: dict):
        self._scene_get_data = scene_get_data
        self.actions = [ActionGet(action_data) for action_data in self._scene_get_data['actions']]

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


class Scene:
    """
    Hue Scene Control Class
    """
    def __init__(self, bridge: Bridge, scene_id_v2: str):
        self.bridge = bridge
        self.scene_id: str = scene_id_v2

    def _get(self) -> dict:
        return self.bridge.get_scene(self.scene_id)

    def _set(self, scene_property: str, data: Union[list, dict]) -> List[dict]:
        return self.bridge.set_scene(self.scene_id, scene_property, data)

    @property
    def data(self) -> SceneGet:
        return SceneGet(self._get())
    
    @property
    def id(self) -> str:
        return self.scene_id

    @property
    def actions(self) -> list:
        return self._get()['actions']

    @actions.setter
    def actions(self, action_items: List[dict]):
        self._set('actions', action_items)

    @property
    def recall(self) -> dict:
        return self._get()['recall']

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


class ActionGet:
    def __init__(self, action_get_data: dict):
        self._target: dict = action_get_data['target']
        self._action: dict = action_get_data['action']

    @property
    def target_rid(self) -> str:
        return self._target['rid']

    @property
    def target_rtype(self) -> str:
        return self._target['rtype']

    @property
    def on(self) -> bool:
        return self._action['on']['on']

    @property
    def color(self):
        return self._action['color']

    @property
    def color_xy(self) -> dict:
        return self._action['color']['xy']

    @property
    def color_temperature(self) -> dict:
        return self._action['color_temperature']

# class Action:
#     def __init__(self, action: dict):
#         self.action: dict = action
#
#     @property
#     def on(self) -> bool:
#         return self.action['on']['on']

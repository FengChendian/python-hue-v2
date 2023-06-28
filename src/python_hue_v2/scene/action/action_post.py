from typing import Optional, Union, Tuple
from ..target import Target
from .action import Action


class ActionPost:
    def __init__(self, action_post_data: dict):
        self._action_post_data = action_post_data
        self._target: dict = action_post_data['target']
        self.target = Target(self._target)

        self._action: dict = action_post_data['action']
        self.action = Action(self._action)

    @property
    def data_dict(self) -> dict:
        return self._action_post_data

    @classmethod
    def create_by_parameters(
        cls,
        target_rid: str,
        target_rtype : str,
        on: bool = False,
        brightness: float = 50.0,
        color_xy: Union[Tuple[float, float], None] = (0.5, 0.5),
        mirek: Optional[int] = None,
    ):
        action_post_data = {}
        action: Action = Action.create_by_parameters(on, brightness, color_xy=color_xy, mirek=mirek)
        action_post_data['action'] = action.data_dict
        action_post_data['target'] = {'rid': target_rid, 'rtype': target_rtype}
        return cls(action_post_data)

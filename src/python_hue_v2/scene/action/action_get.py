from ..target import Target
from .action import Action


class ActionGet:
    def __init__(self, action_get_data: dict):
        self._data_dict = action_get_data

        self._target: dict = action_get_data['target']
        self.target = Target(self._target)

        self._action: dict = action_get_data['action']
        self.action = Action(self._action)

    @property
    def data_dict(self) -> dict:
        return self._data_dict

    @property
    def on(self) -> bool:
        return self.action.on.on

from ..target import Target
from .action import Action


class ActionPut:
    def __init__(self, action_put_data: dict):
        self._action_put_data = action_put_data
        self._target: dict = action_put_data['target']
        self.target = Target(self._target)

        self._action: dict = action_put_data['action']
        self.action = Action(self._action)

    @property
    def data_dict(self) -> dict:
        return self._action_put_data

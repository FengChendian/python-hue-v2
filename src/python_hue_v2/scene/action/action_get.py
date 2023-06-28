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

    @DeprecationWarning
    @property
    def target_rid(self) -> str:
        return self._target['rid']

    @DeprecationWarning
    @property
    def target_rtype(self) -> str:
        return self._target['rtype']

    @property
    def on(self) -> bool:
        return self.action.on.on

    @DeprecationWarning
    @property
    def color(self):
        return self._action['color']

    @DeprecationWarning
    @property
    def color_xy(self) -> dict:
        return self._action['color']['xy']

    @DeprecationWarning
    @property
    def color_temperature(self) -> dict:
        return self._action['color_temperature']

from .target import Target
from .action import Action


class ActionGet:
    def __init__(self, action_get_data: dict):
        self._target: dict = action_get_data['target']
        self.target = Target(self._target)

        self._action: dict = action_get_data['action']
        self.action = Action(self._action)

    @DeprecationWarning
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

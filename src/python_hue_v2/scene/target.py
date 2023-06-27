from typing import Dict


class Target:
    def __init__(self, target_property: Dict):
        self._rid: str = target_property['rid']
        self._rtype: str = target_property['rtype']

    @property
    def rid(self) -> str:
        return self._rid

    @property
    def rtype(self) -> str:
        return self._rtype

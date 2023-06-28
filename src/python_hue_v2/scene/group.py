class Group:
    def __init__(self, data: dict):
        self._rid: str = data['rid']
        self._rtype: str = data['rtype']

    @property
    def rid(self) -> str:
        return self._rid

    @property
    def rtype(self) -> str:
        return self._rtype
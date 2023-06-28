class ResourceIdentifierGet:
    def __init__(self, data: dict) -> None:
        self._data_dict = data
        self._rid: str = data['rid']
        self._rtype: str = data['rtype']

    @property
    def data_dict(self) -> dict:
        return self._data_dict
    
    @property
    def rid(self) -> str:
        return self.rid

    @property
    def rtype(self) -> str:
        return self.rtype

from .resource_identifier_get import ResourceIdentifierGet


class ZoneGet:
    def __init__(self, data: dict) -> None:
        self._data_dict = data
        self._id: str = self._data_dict['id']
        self._children: ResourceIdentifierGet = [ResourceIdentifierGet(child) for child in data['children']]

    @property
    def data_dict(self):
        return self._data_dict

    @property
    def id(self):
        return self._id

    @property
    def children(self):
        return self._children

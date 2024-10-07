class Image:
    def __init__(self, data: dict) -> None:
        self.rid = data.get('rid')
        self.rtype = data.get('rtype')


class MetaData:
    def __init__(self, meta_data: dict) -> None:
        self.name = meta_data['name']
        self.image = Image(meta_data['image']) if 'image' in meta_data.keys() else None
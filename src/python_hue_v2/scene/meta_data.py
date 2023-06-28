class Image:
    def __init__(self, data: dict) -> None:
        self.rid = data.get('rid')
        self.rtype = data.get('rtype')

class Metadata:
    def __init__(self, data:dict) -> None:
        self.name = data['name']
        self.image = Image(data['image']) if 'image' in data.keys() else None
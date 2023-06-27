from typing import Dict, List


class On:
    def __init__(self, on: Dict):
        self.on: bool = on['on']


class Dimming:
    def __init__(self, dimming: Dict):
        self.brightness: float = dimming['brightness']


class ColorXY:
    def __init__(self, xy: dict):
        self.x: float = xy['x']
        self.y: float = xy['y']


class Color:
    def __init__(self, color: Dict):
        self.xy: ColorXY = color['xy']


class ColorTemperature:
    def __init__(self, color_temperature: dict):
        self.mirek = color_temperature['mirek']


class GradientPointGet:
    def __init__(self, gradient_point_get: dict):
        self.color: Color = Color(gradient_point_get['color'])


class Gradient:

    def __init__(self, gradient: dict):
        self.points: List[GradientPointGet] = [GradientPointGet(point) for point in gradient['points']]
        self.mode: str = gradient['mode']


class Effects:
    def __init__(self, effects: dict):
        self.effect: str = effects['effect']


class Dynamics:
    def __init__(self, dynamics: dict):
        self.duration: int = dynamics['duration']


class Action:
    def __init__(self, action: Dict):
        self.on = On(action['on'])
        self.dimming = Dimming(action['dimming'])
        self.color = Color(action['color'])
        self.color_temperature = ColorTemperature(action['color_temperature'])
        self.gradient = Gradient(action['gradient'])
        self.effects = Effects(action['effects'])
        self.dynamics = Dynamics(action['dynamics'])

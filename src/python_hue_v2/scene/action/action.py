from typing import Dict, List, Optional, Union


class On:
    def __init__(self, on: Dict):
        self.on: Optional[bool] = on['on']


class Dimming:
    def __init__(self, dimming: Dict):
        self.brightness: Optional[float] = dimming['brightness']


class ColorXY:
    def __init__(self, xy: dict):
        self.x: Optional[float] = xy.get('x')
        self.y: Optional[float] = xy.get('y')


class Color:
    def __init__(self, color: dict):
        self.xy: ColorXY = ColorXY(color.get('xy'))


class ColorTemperature:
    def __init__(self, color_temperature: dict):
        self.mirek: Optional[int] = color_temperature['mirek']


class GradientPointGet:
    def __init__(self, gradient_point_get: dict):
        self.color: Color = Color(gradient_point_get.get('color'))


class Gradient:
    def __init__(self, gradient: dict):
        self.points: List[GradientPointGet] = [GradientPointGet(point) for point in gradient['points']]
        self.mode: str = gradient['mode']


class Effects:
    def __init__(self, effects: dict):
        self.effect: str = effects['effect']


class Dynamics:
    def __init__(self, dynamics: dict):
        self.duration: Optional[int] = dynamics['duration']


class Action:
    def __init__(self, action: dict):
        self._data_dict: dict = action
        self.keys = action.keys()

        self.on = On(action['on']) if 'on' in self.keys else None
        self.dimming = Dimming(action['dimming']) if 'dimming' in self.keys else None
        self.color = Color(action['color']) if 'color' in self.keys else None
        self.color_temperature = (
            ColorTemperature(action['color_temperature']) if 'color_temperature' in self.keys else None
        )
        self.gradient = Gradient(action['gradient']) if 'gradient' in self.keys else None
        self.effects = Effects(action['effects']) if 'effects' in self.keys else None
        self.dynamics = Dynamics(action['dynamics']) if 'dynamics' in self.keys else None

    @classmethod
    def create_by_parameters(
        cls,
        on: bool = False,
        brightness: float = 50.0,
        color_xy: Union[tuple, None] = (0.5, 0.5),
        mirek: Optional[int] = None,
    ):
        action = {
            'on': {'on': on},
            'dimming': {'brightness': brightness},
        }
        if mirek is not None:
            action['color_temperature'] = {'mirek': mirek}
        elif color_xy is not None:
            action['color'] = {'xy': {'x': color_xy[0], 'y': color_xy[1]}}

        return cls(action)

    @property
    def data_dict(self) -> dict:
        return self._data_dict

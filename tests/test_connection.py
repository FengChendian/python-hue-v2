import time

from python_hue_v2 import Hue, Light, BridgeFinder, Scene

finder = BridgeFinder()
time.sleep(1)

test_hostname = finder.get_bridge_server_lists()[0]
test_key = '7K-IbBzEV3wZoXkTlSh6HyLTALLFsYrxCjIcW1o9'
hue = Hue(test_hostname, test_key)


def test_light_on():
    assert hue is not None
    lights = hue.lights
    for light in lights:
        assert type(light.on) is bool
    # for light in lights:
    #     light.on = True
    # time.sleep(1)
    # for light in lights:
    #     light.on = False


def test_light_brightness():
    assert type(hue.lights[0].brightness) is float


def test_light_color_xy():
    assert type(hue.lights[0].color_xy) is dict
    assert type(hue.lights[0].color_xy['x']) is float
    assert type(hue.lights[0].color_xy['y']) is float


def test_scenes():
    assert hue.scenes[0].type == 'scene'

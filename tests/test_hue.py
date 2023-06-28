import time
import json
from src.python_hue_v2.grouped_light import GroupedLight
from src.python_hue_v2.scene import ActionPost
from src.python_hue_v2.scene import ScenePost
from src.python_hue_v2 import Hue, Light, BridgeFinder, Scene

finder = BridgeFinder()
time.sleep(1)
test_hostname = finder.get_bridge_server_lists()[0]
test_key = '7K-IbBzEV3wZoXkTlSh6HyLTALLFsYrxCjIcW1o9'
hue = Hue(test_hostname, test_key)


def test_bridge_connect():
    hue_test = Hue(test_hostname)
    try:
        hue_test.bridge.connect()
    except ConnectionError as e:
        print(e)
    assert 1


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
    if len(hue.scenes) > 0:
        assert hue.scenes[0].type == 'scene'
    else:
        assert 1


def test_create_scene():
    with open('./tests/create_scene_config.json', 'r', encoding="utf-8") as f:
        data = json.load(f)
    light_id = []
    lights = hue.lights
    for light in lights:
        light_id.append(light.light_id)

    actions = []
    for rid in light_id:
        actions.append(
            ActionPost.create_by_parameters(
                target_rid=rid,
                target_rtype='light',
                on=True,
                brightness=data['2']['bri'],
                color_xy=(data['2']['xy'][0], data['2']['xy'][1])
                # brightness=data['1']['bri'],
                # mirek=data['1']['ct'],
            )
        )

    rooms = hue.rooms
    scene_post: ScenePost = ScenePost.create_by_parameters(
        actions=actions, name='test', group_rid=rooms[0].id, group_rtype="room"
    )
    hue.create_scene(scene_post)
    assert 1


def test_recall_scene():
    scenes = hue.scenes
    test_scene = None
    for scene in scenes:
        if scene.meta_data.name == 'test':
            test_scene = scene
            break
    test_scene.recall()
    time.sleep(3)
    groups = hue.grouped_lights
    test_group = None
    for group in groups:
        if group.owner.rid == test_scene.group.rid:
            test_group = group
    if test_group:
        test_group.on = False
    else:
        assert False


def test_delete_scene():
    scenes = hue.scenes
    test_scene = None
    for scene in scenes:
        if scene.meta_data.name == 'test':
            test_scene = scene
            break

    hue.bridge.delete_scene(test_scene.id)
    assert 1

# def test_grouped_light_type():
#     assert hue.grouped_lights[0].type == 'grouped_light'


# def test_grouped_light_brightness():
#     assert type(hue.grouped_lights[0].brightness) == float
#     hue.grouped_lights[0].on = True
#     hue.grouped_lights[0].brightness = 70.0
#     # Rounding error
#     assert hue.grouped_lights[0].brightness - 70.0 < 1
#     hue.grouped_lights[0].on = False

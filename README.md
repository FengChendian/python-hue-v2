# Python Hue V2

Python library to control the Philips Hue lighting system
for [Hue-V2](https://developers.meethue.com/develop/hue-api-v2/api-reference/) API.

## Features

- Design for Hue API 2.0

## High Level Control

### Simple Example

```python
import time
from python_hue_v2 import Hue, BridgeFinder

finder = BridgeFinder()
time.sleep(1)  # wait for search
# Get server by mdns
host_name = finder.get_bridge_server_lists()[0]  # Here we use first Hue Bridge
addresses = finder.get_bridge_addresses()
# or hue = Hue('ip address','app-key')
hue = Hue(addresses[0], 'hue app key')  # create Hue instance

# If you don't have hue-app-key, press the button and call bridge.connect() (this only needs to be run a single time)
# hue = Hue(host_name)
# app_key = hue.bridge.connect() # you can get app_key and storage on disk

lights = hue.lights

for light in lights:
    print(light.on)
    light.on = True
    light.brightness = 80.0
```

### Scenes

You can get scenes from hue bridge.

```python
from python_hue_v2 import Hue

hue = Hue('bridge-ip', 'app-key')

scenes = hue.scenes
for scene in scenes:
    print(scene.id)
    print(scene.data_dict)
```

Recall scene using `active`, `dynamic_palette`, `static`.

```python
scene = scenes[0]
scene.recall(action='active')
```

If you want create one scene with light actions in a room:

```python
from python_hue_v2.scene import ActionPost, ScenePost

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
            brightness=50,
            color_xy=(0.1, 0.3)  # xy color tuple
            # mirek=200 % or use mirek
        )
    )

# Get all rooms, may be empty
rooms = hue.rooms

# ScenePost should have a group property, here we bind with a room

# refer to https://developers.meethue.com/develop/hue-api-v2/api-reference/#resource_scene_post
# Group associated with this Scene. All services in the group are part of this scene. 
# If the group is changed the scene is update (e.g. light added/removed)
scene_post: ScenePost = ScenePost.create_by_parameters(
    actions=actions, name='test', group_rid=rooms[0].id, group_rtype="room"
)
hue.create_scene(scene_post)
```

Also, you can delete scene by id.

```python
hue.delete_scene('scene-id-example')
```

### Grouped Light

Get group Lights from hue.

```python
from python_hue_v2 import Hue

hue = Hue('bridge-ip', 'app-key')
grouped_lights = hue.grouped_lights

for group in grouped_lights:
    print(group.type)
    # group.on = True
    group.set_state(True, 100, None) 
    group.set_state(on=True, brightness=100, duration_ms=1) # Feature in version 2.0.1
    
```

## Low Level Control

> Low level function may be changed when update

You can use some basic functions in this library. 

For example, you can use `get_lights`,`set_light` or other low level control functions to implement
some custom functions.

```python
import time
from python_hue_v2 import Hue

# or hue = Hue('ip address','app-key')
hue = Hue('host_name', 'hue app key')  # create Hue instance
bridge = hue.bridge

bridge.get_lights()
bridge.set_light('id', light_property_name='on', property_value={'on': True})

bridge.get_zones()
```

## Attention

Some API may be de deprecated When major version updates.

- Grouped light API will be changed after version `2.0.0`

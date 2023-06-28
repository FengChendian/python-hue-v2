# Python Hue V2

Python library to control the Philips Hue lighting system for Hue-V2 API.

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

# or hue = Hue('ip address','app-key')
hue = Hue(host_name, 'hue app key')  # create Hue instance

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

### Grouped Light
Get Lights from hue.
```python
from python_hue_v2 import Hue

hue = Hue('bridge-ip', 'app-key')
grouped_lights = hue.grouped_lights

for group in grouped_lights:
    print(group.type)
```

## Low Level Control
Also, you can use basic function in bridge class.
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

## TODO

- Zones Control Class

# Python Hue V2

Python library to control the Philips Hue lighting system for Hue-V2 API.

## Features

- Design for Hue API 2.0

## Usage

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
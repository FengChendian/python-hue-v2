import time
from unittest import TestCase

from python_hue_v2 import Hue, BridgeFinder

finder = BridgeFinder()
time.sleep(1)
test_hostname = finder.get_bridge_server_lists()[0]
test_key = '7K-IbBzEV3wZoXkTlSh6HyLTALLFsYrxCjIcW1o9'
hue = Hue(test_hostname, test_key)


class IntegrationTests(TestCase):
    def test_set_on_grouped_light(self):
        grouped_lights = hue.grouped_lights
        grouped_light = grouped_lights[0]

        test_cases = [
            True,
            False,
        ]

        for is_on in test_cases:
            with self.subTest(is_on=is_on):
                grouped_light.on = is_on
                time.sleep(1)

    def test_set_brightness_grouped_light(self):
        grouped_lights = hue.grouped_lights
        grouped_light = grouped_lights[0]
        grouped_light.on = True

        test_cases = [
            30,
            50,
            100
        ]

        for brightness in test_cases:
            with self.subTest(brightness=brightness):
                grouped_light.brightness = brightness
                time.sleep(1)

    def test_set_state_grouped_light(self):
        grouped_lights = hue.grouped_lights
        grouped_light = grouped_lights[0]

        test_cases = [
            (True, 100, 6000),
            (False, 50, 3000),
            (True, 100, None),
            (False, None, None),
            (True, None, None),
        ]

        for is_on, brightness, duration in test_cases:
            with self.subTest(is_on=is_on, brightness=brightness, duration=duration):
                grouped_light.set_state(is_on, brightness, duration)
                time.sleep(duration / 1000 if duration else 1)

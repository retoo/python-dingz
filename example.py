"""Sample code to use the wrapper for interacting with the dingz device."""
import asyncio
import logging

from dingz.dingz import Dingz
from dingz.discovery import discover_dingz_devices


IP_ADDRESS = "192.168.0.103"


async def main():
    """Sample code to work with a dingz unit."""
    # Discover dingz devices
    devices = await discover_dingz_devices()

    print(f"Found {len(devices)} devices")
    for device in devices:
        print(
            f"  MAC address: {device.mac}, IP address: {device.host}, HW: {device.hardware}"
        )

    # Work with one dingz unit
    async with Dingz(IP_ADDRESS) as dingz:

        # Collect the data of the current state
        await dingz.get_device_info()
        print("Device details:", dingz.device_details)

        # Get all details
        await dingz.get_settings()
        print("All device details:", dingz.settings)

        # Get the configuration
        # Available: pir, input, themostat
        await dingz.get_configuration("pir")
        print("Configuration:", dingz.configuration)

        # Get the temperature
        await dingz.get_temperature()
        print("Temperature:", dingz.temperature)

        # Get data from the PIR
        await dingz.get_light()
        print("Brightness:", dingz.intensity)
        # Is it day?
        print("Day?:", dingz.day)
        # Motion detected
        print("Motion?:", dingz.motion)

        # Collect the data of the current state
        await dingz.get_button_action()
        print("Button actions:", dingz.button_action)

        # # Turn on the front LED
        print("Turning Front LED on...")
        await dingz.turn_on()
        await asyncio.sleep(3)
        print("Front LED:", await dingz.enabled())
        await dingz.turn_off()
        print("Front LED:", await dingz.enabled())


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

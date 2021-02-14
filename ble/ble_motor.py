import argparse
import asyncio

import bleak
from bleak import BleakClient

# UART service UUID
CHARACTERISTIC_UUID_RX = "6E400002-B5A3-F393-E0A9-E50E24DCCA9E"
# BLE MAC ADDRESS
ADDRESS = "F0:08:D1:C8:A1:5E"

class BleMotor:
    def __init__(self, loop, address=ADDRESS, write_uuid=CHARACTERISTIC_UUID_RX):
        self.loop       = loop
        self.address    = address
        self.write_uuid = write_uuid
        self.client     = None

    async def connect(self):
        while True:
            try:
                self.client = BleakClient(self.address)
                await self.client.connect()
                connected = await self.client.is_connected() # is connected?
                print(f"Connected: {connected}") # connected = True or False
                return connected
            except bleak.exc.BleakDotNetTaskError:
                print("reconnecting...")
                continue

    async def disconnect(self):
        disconnected = await self.client.disconnect()
        print(f"Disconnected: {disconnected}")
        return disconnected

    async def write(self, motor_num, angle):
        write_value = str(motor_num) + " " + str(angle)
        while True:
            try:
                await self.client.write_gatt_char(self.write_uuid, bytearray(write_value.encode()))
                break
            except bleak.exc.BleakDotNetTaskError:
                print("reconnecting...")
                await self.connect() # reconnect

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--angle", "-a", type=str, default="90", help="motor angle")
    parser.add_argument("--motor", "-m", type=str, default="1", help="motor number(0~2)")
    args = parser.parse_args()

    loop = asyncio.get_event_loop()
    ble_motor = BleMotor(loop)
    loop.run_until_complete(ble_motor.connect())
    loop.run_until_complete(ble_motor.write(args.motor, args.angle))
    loop.run_until_complete(ble_motor.disconnect())

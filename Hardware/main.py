from time import sleep
import RPi.GPIO as GPIO
import asyncio
import websockets

GPIO.setmode(GPIO.BCM)

async def start():
    uri = "ws://lookalivesunshine.tech:81"
    async with websockets.connect(uri) as websocket:
        await websocket.send("pi")
        await websocket.recv()

        interval = 0.02

        GPIO.setup(2, GPIO.OUT)
        GPIO.output(2, False)
        sleep(interval)
        GPIO.cleanup()


asyncio.get_event_loop().run_until_complete(start())

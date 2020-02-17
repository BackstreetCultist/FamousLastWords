from time import sleep
import RPi.GPIO as GPIO
import asyncio
import websockets
import constant

#Don't touch these
UPMOTOR = 2
LEFTEYE = 3
RIGHTEYE = 4
DOWNMOTOR = 5

def setGPIOs():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(UPMOTOR, GPIO.OUT)
    GPIO.setup(LEFTEYE, GPIO.OUT)
    GPIO.setup(RIGHTEYE, GPIO.OUT)
    GPIO.setup(DOWNMOTOR, GPIO.OUT)

def act():
        GPIO.output(UPMOTOR, False)
        sleep(0.50)
        GPIO.output(UPMOTOR, True)

        GPIO.output(LEFTEYE, True)
        GPIO.output(RIGHTEYE, True)
        sleep(5.00)
        GPIO.output(LEFTEYE, False)
        GPIO.output(RIGHTEYE, False)

        GPIO.output(DOWNMOTOR, False)
        sleep(0.50)
        GPIO.output(DOWNMOTOR, True)




async def start():
    uri = "ws://lookalivesunshine.tech:81"
    async with websockets.connect(uri) as websocket:
        await websocket.send("pi")
        await websocket.recv()

        print("Pi working")
        act()


print("Setting GPIOs")
setGPIOs()
print("Sleeping")
sleep(5)
#asyncio.get_event_loop().run_until_complete(start())
print("Acting")
act()
print("Done acting")
GPIO.cleanup()
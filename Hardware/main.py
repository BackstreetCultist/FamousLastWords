from time import sleep
import RPi.GPIO as GPIO
import asyncio
import websockets

#uri = "ws://lookalivesunshine.tech:80"

uri ="ws://famouslastwords.dummybug.com:80"

eyesopen = False

#Don't touch these
UPMOTOR = 2
LEFTEYE = 3
RIGHTEYE = 4
DOWNMOTOR = 5

def setGPIOs():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(UPMOTOR, GPIO.IN)
    GPIO.setup(LEFTEYE, GPIO.OUT)
    GPIO.setup(RIGHTEYE, GPIO.OUT)
    GPIO.setup(DOWNMOTOR, GPIO.OUT)

def act():
    global eyesopen
    if not eyesopen:
        GPIO.setup(UPMOTOR, GPIO.OUT)
        GPIO.output(UPMOTOR, True)
        sleep(0.50)
        GPIO.setup(UPMOTOR, GPIO.IN)
        eyesopen = True

    GPIO.output(LEFTEYE, True)
    GPIO.output(RIGHTEYE, True)
    sleep(5.00)
    GPIO.output(LEFTEYE, False)
    GPIO.output(RIGHTEYE, False)

    GPIO.output(DOWNMOTOR, False)
    sleep(0.50)
    GPIO.output(DOWNMOTOR, True)

async def start():
    while True:
        async with websockets.connect(uri) as websocket:
            await websocket.recv()
            print("Pi working")
            act()
        #GPIO.cleanup()


#setGPIOs()
#act();
#GPIO.cleanup()
    print("Setting GPIOs")
setGPIOs()
try:
    asyncio.get_event_loop().run_until_complete(start())
except KeyboardInterrupt:
    GPIO.cleanup()


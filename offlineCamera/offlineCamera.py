from gpiozero import MotionSensor
import picamera
from signal import pause
from time import sleep
from datetime import datetime

print('setting up camera')
camera = picamera.PiCamera()
camera.resolution = (1920, 1080)
camera.vflip = True
camera.hflip = True
camera.sharpness = 100
camera.exposure_mode = 'auto'
camera.meter_mode = 'average'
camera.awb_mode = 'auto'
numberOfPicturesToTake = 30
secondsBetweenPictures = .5
print('setting up motion sensor')
pir = MotionSensor(4)


def countdown(seconds):
    for second in range(seconds):
        print(str(seconds - seconds) + ' seconds to go')
        sleep(1)


def takePictures():
    print('motion registered, taking pictures')
    for pictures in range(numberOfPicturesToTake):
        timestamp = datetime.now().timestamp()
        camera.capture(str(timestamp) + '.jpg')
        sleep(secondsBetweenPictures)
    print('pictures taken, waiting for motion')



pir.when_motion = takePictures
pause()

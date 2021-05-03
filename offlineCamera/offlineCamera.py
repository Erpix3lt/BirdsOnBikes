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
        filename = './capturedImages/' + str(datetime.now().timestamp()) + '.jpg'
        camera.capture(filename)
        # sleep(secondsBetweenPictures) # the raspberry zero needs ~0.5 seconds to take and save a picture
    print('pictures taken, waiting for motion')



pir.when_motion = takePictures
pause()

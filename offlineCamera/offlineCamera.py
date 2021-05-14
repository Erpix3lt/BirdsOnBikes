import picamera
import os
from gpiozero import MotionSensor
from signal import pause
from time import sleep
from datetime import datetime

currentDate = datetime.now().date()
print('setting up camera')
camera = picamera.PiCamera()
camera.resolution = (1920, 1080)
camera.vflip = True
camera.hflip = True
camera.sharpness = 100
camera.exposure_mode = 'auto'
camera.meter_mode = 'average'
camera.awb_mode = 'auto'
pictureNumber = 0
numberOfPicturesToTake = 30
secondsBetweenPictures = .5

print('setting up motion sensor')
pir = MotionSensor(23, queue_len=50, sample_rate=100,threshold=.9)

def takePictures():
    global pictureNumber
    savePath = './capturedImages/' + getCurrentDateString() + '/'
    if (os.path.exists(savePath) == False):
        os.mkdir(savePath)
    print('motion registered, taking pictures')
    for pictures in range(numberOfPicturesToTake):
        pictureNumber += 1
        filename = savePath + str(pictureNumber).rjust(5, '0') + '.jpg'
        camera.capture(filename, format='jpeg', quality=50, thumbnail=None)
        # sleep(secondsBetweenPictures) # the raspberry zero needs ~0.5 seconds to take and save a picture
    print('pictures taken, waiting for motion')

def getCurrentDateString():
    global currentDate
    global pictureNumber
    newDate = datetime.now().date()
    if (currentDate != newDate):
        currentDate = newDate
        pictureNumber = 0

    return str(currentDate.year) + '-' + str(currentDate.month) + '-' + str(currentDate.day)

print(getCurrentDateString())

pir.when_motion = takePictures
pause()
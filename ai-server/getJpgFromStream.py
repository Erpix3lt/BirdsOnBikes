import cv2
from datetime import datetime
import time

streamURL = 'https://stream.birdsh.it/stream/video.mjpeg'
cap = cv2.VideoCapture(streamURL)

while True:
  
  ret, frame = cap.read()
  dateTimeObj = datetime.now
  imageFileName = time.strftime('./capturedImages/%Y-%m-%d-%H:%M:%S.jpg')
  cv2.imwrite(imageFileName, frame)
  if cv2.waitKey(1) == 27:
    exit(0)
  time.sleep(1)
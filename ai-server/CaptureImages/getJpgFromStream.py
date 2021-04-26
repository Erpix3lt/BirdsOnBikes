import cv2
from time import sleep

streamURL = 'https://stream.birdsh.it/stream/video.mjpeg'
cap = cv2.VideoCapture(streamURL)
counter = 0
while True:
  counter = counter + 1
  if counter < 10:
    imageFileName = './capturedImages/image-0000' + str(counter) + '.jpg'
  elif counter < 100:
    imageFileName = './capturedImages/image-000' + str(counter) + '.jpg'
  elif counter < 1000:
    imageFileName = './capturedImages/image-00' + str(counter) + '.jpg'
  elif counter < 10000:
    imageFileName = './capturedImages/image-0' + str(counter) + '.jpg'
  else:
    imageFileName = './capturedImages/image-' + str(counter) + '.jpg'
  ret, frame = cap.read()
  cv2.imwrite(imageFileName, frame)
  sleep(1)

import cv
import time
from SimpleCV import *
from collections import deque
capture = cv.CaptureFromFile("limithd.avi")
buf = deque([])
while True:
  img = Image(cv.QueryFrame(capture))  
  buf.append(img)
  if len(buf) == 5:
    buf.popleft().findBlobs().show(autocolor=True)

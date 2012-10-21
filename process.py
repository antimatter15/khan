import cv
cv.NamedWindow("Video", cv.CV_WINDOW_AUTOSIZE)
capture = cv.CaptureFromFile("newton.avi")
lastone = None
while True:
  src_img = cv.QueryFrame(capture)
  bw_img = cv.CreateImage((src_img.width, src_img.height), cv.IPL_DEPTH_8U, 1)
  cv.CvtColor(src_img, bw_img, cv.CV_RGB2GRAY)
  img = cv.CreateImage((src_img.width, src_img.height), cv.IPL_DEPTH_8U, 1)
  cv.Threshold(bw_img, img, 250, 255, cv.CV_THRESH_BINARY)
  """
  if lastone:
    cv.AbsDiff(lastone, bw_img, img)
  else:
    img = bw_img
  lastone = bw_img"""
  eig_image = cv.CreateMat(img.width, img.height, cv.CV_32FC1)
  temp_image = cv.CreateMat(img.width, img.height, cv.CV_32FC1)
  for (x,y) in cv.GoodFeaturesToTrack(img, eig_image, temp_image, 10, 0.04, 1.0, useHarris = True):
    print "good feature at", x,y
    cv.Circle(img, (int(x), int(y)), 20, cv.Scalar(255))
  cv.ShowImage("Video", img)
  cv.WaitKey(10)

import numpy
import cv2

ImagesDir = "testImages"
ImageName = "airplane.png"

image = cv2.imread(ImagesDir + "/" + ImageName)

imageAfterBlur = cv2.blur(image, (30, 30))

cv2.imshow("IMG", imageAfterBlur)
cv2.waitKey(0)

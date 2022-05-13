import cv2 as cv

img = cv.imread("tesla.jpg")

cv.imshow("Output", img)
cv.waitKey(0)

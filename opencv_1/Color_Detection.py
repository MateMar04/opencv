import cv2 as cv
import numpy as np


def empty(a):
    pass


cv.namedWindow("Trackbars")
cv.resizeWindow("Trackbars", 640, 240)

cv.createTrackbar("Hue Min", "Trackbars", 161, 179, empty)
cv.createTrackbar("Hue Max", "Trackbars", 179, 179, empty)
cv.createTrackbar("Sat Min", "Trackbars", 44, 255, empty)
cv.createTrackbar("Sat Max", "Trackbars", 255, 255, empty)
cv.createTrackbar("Val Min", "Trackbars", 52, 255, empty)
cv.createTrackbar("Val Max", "Trackbars", 255, 255, empty)

while True:
    img = cv.imread("tesla.jpg")
    imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    h_min = cv.getTrackbarPos("Hue Min", "Trackbars")
    h_max = cv.getTrackbarPos("Hue Max", "Trackbars")
    s_min = cv.getTrackbarPos("Sat Min", "Trackbars")
    s_max = cv.getTrackbarPos("Sat Max", "Trackbars")
    v_min = cv.getTrackbarPos("Val Min", "Trackbars")
    v_max = cv.getTrackbarPos("Val Max", "Trackbars")
    print(h_min, h_max, s_min, s_max, v_min, v_max)

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    mask = cv.inRange(imgHSV, lower, upper)

    imgResult = cv.bitwise_and(img, img, mask=mask)

    cv.imshow("Image", img)
    cv.imshow("HSV Image", imgHSV)
    cv.imshow("Mask Image", mask)
    cv.imshow("Result Image", imgResult)

    cv.waitKey(1)

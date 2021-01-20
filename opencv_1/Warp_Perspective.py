import cv2 as cv
import numpy as np

img = cv.imread("card.jpg")
print(img.shape)

imgRezised = cv.resize(img, (500, 500))

width, height = 500, 250
pts1 = np.float32([[147, 39], [412, 148], [63, 165], [342, 290]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv.getPerspectiveTransform(pts1, pts2)

imgPerspective = cv.warpPerspective(imgRezised, matrix, (width, height))

cv.imshow("Image", imgRezised)
cv.imshow("Image", imgPerspective)

cv.waitKey(0)

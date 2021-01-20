import cv2 as cv
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)

#img[:] = 255, 0, 0

cv.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 3) #linea diagonal
cv.rectangle(img, (0, 0), (250, 300), (0, 0, 255), 3) #Rectangulo
cv.circle(img, (400, 50), 30, (255, 255, 0), 3) #Circulo
cv.putText(img, "HELLO", (100, 100), cv.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 3)


cv.imshow("Image", img)

cv.waitKey(0)

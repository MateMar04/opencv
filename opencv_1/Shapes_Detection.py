import cv2 as cv
import numpy as np

def getContours(img):
    countours, hierarchy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

    for cnt in countours:
        area = cv.contourArea(cnt)
        print(area)

        if area > 500:
            cv.drawContours(imgContour, cnt, -1, (255, 0, 0), 4)
            perimeter = cv.arcLength(cnt, True)
            #print(perimeter)
            approx = cv.approxPolyDP(cnt, 0.01 * perimeter, True)
            print(len(approx))
            obj_corner = len(approx)
            x, y, w, h = cv.boundingRect(approx)

            if obj_corner == 3:
                object_type = "Triangle"
            elif obj_corner == 4:
                object_type = "Sq"
            else: object_type = "NONE"

            cv.rectangle(imgContour, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv.putText(imgContour, object_type, (x + (w // 2) - 10, y + (h // 2) - 100),cv.FONT_HERSHEY_COMPLEX,0.5, (0, 0, 0), 2)


img = cv.imread("shapes.png")
imgContour = img.copy()

imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
imgBlur = cv.GaussianBlur(imgGray, (7, 7), 1)
imgCanny = cv.Canny(imgBlur, 150, 150)
getContours(imgCanny)

cv.imshow("Shapes", img)
cv.imshow("Gray", imgGray)
cv.imshow("Blur", imgBlur)
cv.imshow("Canny", imgCanny)
cv.imshow("Contours", imgContour)
cv.waitKey(0)


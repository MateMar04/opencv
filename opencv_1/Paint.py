import cv2 as cv
import numpy as np

frame_width = 640
frame_height = 480

cap = cv.VideoCapture(0)
cap.set(3, frame_width)
cap.set(4, frame_height)
cap.set(10, 0)

colors = [[42, 80, 142, 85, 255, 255],
          [30, 82, 192, 31, 255, 255],
          [2, 195, 248, 27, 255, 255],
          [105, 146, 116, 130, 255, 255]]

color_values = [[59, 255, 131],
                [59, 229, 255],
                [0, 128, 255],
                [255, 0, 0]]

points = []


def find_color(img, colors, color_values):
    imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    cont = 0
    new_points = []
    for color in colors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv.inRange(imgHSV, lower, upper)
        x, y = get_contours(mask)
        cv.circle(imgResult, (x, y), 10, color_values[cont], cv.FILLED)
        if x != 0 and y != 0:
            new_points.append([x, y, cont])
        cont += 1
        #cv.imshow(str(color[0]), mask)
    return new_points


def get_contours(img):
    contours, hierarchy = cv.findContours(img, cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        area = cv.contourArea(cnt)
        if area > 500:
            #cv.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
            peri = cv.arcLength(cnt, True)
            approx = cv.approxPolyDP(cnt, 0.02 * peri, True)
            x, y, w, h = cv.boundingRect(approx)
    return x + w // 2, y


def draw(points, color_values):
    for point in points:
        cv.circle(imgResult, (point[0], point[1]), 10, color_values[point[2]], cv.FILLED)



while True:
    success, img = cap.read()
    imgResult = img.copy()
    new_points = find_color(img, colors, color_values)
    if len(new_points) != 0:
        for new_point in new_points:
            points.append(new_point)
    if len(points) != 0:
        draw(points, color_values)
    cv.imshow("Result", imgResult)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

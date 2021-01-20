import cv2 as cv
face_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv.imread("face.jpg")
imgGray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(imgGray, 1.1, 4)

for (x, y, w, h) in faces:
    cv.rectangle(img,(x, y), (x + w, y + h), (255, 0, 0), 2)

cv.imshow("Image", img)
cv.waitKey(0)

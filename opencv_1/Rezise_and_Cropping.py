import cv2 as cv

img = cv.imread("tesla.jpg")
print(img.shape)

imgRezised = cv.resize(img, (330, 185))
print(imgRezised.shape)

imgCropped = img[0:200, 200:500]

cv.imshow("Image", img)
cv.imshow("Rezised Image", imgRezised)
cv.imshow("Cropped Image", imgCropped)

import cv2 as cv

img = cv.imread("/home/czdpzc/Desktop/1.png")
cv.imshow("show",img)
cv.waitKey()
print(cv.__version__)
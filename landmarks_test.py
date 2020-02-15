import face_recognition as fc
import cv2 as cv
import time

# image_path = "./data_pic/obama.png"
image_path = "./data_pic/obama-480p.jpg"

image = fc.load_image_file(image_path)
tic = time.time()
face_landmarks_list = fc.face_landmarks(image,model="hog")
toc = time.time()

image_cv = cv.imread(image_path)

# print(face_landmarks_list)


'''
速度可参考location_test.py中的注释.
'''
print(toc-tic)

print(face_landmarks_list.__len__())

for face_landmarks in face_landmarks_list:
    for facial_feature in face_landmarks.keys():
        for (y,x) in face_landmarks[facial_feature]:
            cv.circle(image_cv,(y,x),0,(0,0,255),3,1)

cv.imshow("show",image_cv)
cv.waitKey(0)

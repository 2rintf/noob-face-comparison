import face_recognition as fc
import cv2 as cv
import time

# pic_path = "./data_pic/obama.png"
# pic_path = "./data_pic/obama-480p.jpg"
pic_path = "./data_pic/jordan_web.jpg"

image = fc.load_image_file(pic_path)
tic = time.time()
face_location = fc.face_locations(image,model="hog")
toc = time.time()

print(face_location)

'''
1080p:
        hog: 1.249s
        cnn: 109.448s
720p:
        hog:0.538s
        cnn:44.642s
480p:
        hog:0.234s
        cnn:19.489s
'''
print(toc-tic)

image_raw_cv = cv.imread(pic_path)
# 深拷贝一下
image_cv = cv.copyTo(image_raw_cv,image_raw_cv)
print(image_cv.shape)

for (top,right,bottom,left) in face_location:
    cv.rectangle(image_cv, (left, top), (right, bottom), (0, 0, 255), 1, 1)







# for i in range(3):
#     image_cv = cv.rectangle(image_cv, face_location[i][:2], face_location[i][2:4], (0, 0, 255), 1, 1)

# cv.rectangle(image_cv, (425,32), (487,94), (0, 0, 255), 1, 1)

# rec_img = cv.rectangle(image_cv,(0,0),(50,50),(255,0,0),1,1)

# cv.rectangle(image_cv,face_location[0])
# cv.rectangle(image_cv,face_location[1])
# cv.rectangle(image_cv,face_location[2])

cv.imshow("show1",image_raw_cv)
cv.imshow("show2",image_cv)
cv.waitKey()
# exit()


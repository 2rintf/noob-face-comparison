import face_recognition as fc
import cv2 as cv
import time

path1 = "./data_pic/George_W_Bush_0002.jpg"
path2 = "./data_pic/George_W_Bush_0067.jpg"
path3 = "./data_pic/obama-480p.jpg"

known_image = fc.load_image_file(path1)
unknown_image = fc.load_image_file(path3)


'''
face_encodings 返回图像中每张脸的128维编码
！编码较为耗时，480p 图像编码430ms.
'''
biden_encoding = fc.face_encodings(known_image)[0]
tic = time.time()
unknown_encoding = fc.face_encodings(unknown_image)[0]
toc = time.time()
print(toc-tic)


distance = fc.face_distance([biden_encoding],unknown_encoding)
print(distance)

results = fc.compare_faces([biden_encoding], unknown_encoding)
print(results)
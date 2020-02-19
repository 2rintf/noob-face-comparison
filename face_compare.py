import face_recognition as fc
import cv2 as cv
import time

import numpy as np

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
print(biden_encoding)
tic = time.time()
unknown_encoding = fc.face_encodings(unknown_image)[0]
toc = time.time()
print(toc-tic)

# face_distance的本质。
# !要再套一层list的原因就是，检测出来的脸可能有多张，用来与一张已知的脸
# 比较。
print(np.linalg.norm([biden_encoding]-unknown_encoding,axis=1))

# face_distance 实际上就是返回两个128维编码数组之间的欧式距离，
# 即利用向量的2-范数求欧式距离。
distance = fc.face_distance([biden_encoding],unknown_encoding)
print(distance)

results = fc.compare_faces([biden_encoding], unknown_encoding)
print(results)

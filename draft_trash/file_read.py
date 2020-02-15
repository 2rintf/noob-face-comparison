### 仅尝试！

import os
import cv2 as cv
import face_recognition as fc



base_path = "./data_pic/lfw"
a = os.listdir(base_path)
print(a)
print(len(a))
print(a[0:3])

fs = open("./data_pic/test_pic_list_from_lfw.txt",'w+')


# fc.compare_faces()
true_num_of_pic = 0
for i in range(0,100):
    print(base_path+'/'+a[i]+'/'+a[i]+'_0001.jpg')
    test_path = base_path+'/'+a[i]+'/'+a[i]+'_0001.jpg'

    img = fc.load_image_file(test_path)
    face_location = fc.face_locations(img,model="hog")
    # print(face_location)
    if face_location==[]:
        print('fail to recog')
        continue
    elif len(face_location)>1:
        print('more than 1 face. Pass.')
        continue
    fs.write(test_path+'\n')
    true_num_of_pic+=1
    print('done.')
    # img_cv = cv.imread(test_path)
    # for (top,right,bottom,left) in face_location:
    #     cv.rectangle(img_cv, (left, top), (right, bottom), (0, 0, 255), 1, 1)
    #
    # cv.imshow("show",img_cv)
    # cv.waitKey(1000)

fs.write("# total nums of pic is "+str(true_num_of_pic)+'\n')
fs.close()

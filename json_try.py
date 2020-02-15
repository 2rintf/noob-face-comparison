import json
import os
import cv2 as cv
import face_recognition as fc

base_path = "./data_pic/lfw"
a = os.listdir(base_path)
# print(a)
# print(len(a))
# print(a[0:3])

total = []
total_dict = {'num':0,'path':[]}
# fc.compare_faces()
true_num_of_pic = 0
for i in range(0,2000):
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
    total.append(test_path)
    # true_num_of_pic+=1
    print('done.')

total_dict['num'] = len(total)
total_dict['path'] = total
# print(total_dict)

# indent参数是json用来格式化字典，好看点，数值为0就直接一行。
json = json.dumps(total_dict,indent=4)
# print(json)
fs = open("./data_pic/2000_pic_list.json",'w+')
fs.write(json)
fs.close()
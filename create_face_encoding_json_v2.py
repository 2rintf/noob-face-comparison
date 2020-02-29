import json
import os
import cv2 as cv
import face_recognition as fc
import re
import random

base_path = "./data_pic/lfw"
a = os.listdir(base_path)
# print(a)
# print(len(a))
# print(a[0:3])

total = []
encoding_temp = []
total_dict = {}
info_dict = {'index':0,'name':"",'path':[],'encoding':[],'sex':"",'age':0,'phone':0,'email':""}
# fc.compare_faces()
true_num_of_pic = 0
for i in range(0,3000):
    print(base_path+'/'+a[i]+'/'+a[i]+'_0001.jpg')
    test_path = base_path+'/'+a[i]+'/'+a[i]+'_0001.jpg'

    img = fc.load_image_file(test_path)
    face_location = fc.face_locations(img,model="hog")
    # print(face_location)
    if face_location==[]:
        print('     fail to recog.')
        continue
    elif len(face_location)>1:
        print('     more than 1 face. Pass.')
        continue

    info_dict['path'] = test_path
    info_dict['encoding'] = list(fc.face_encodings(img)[0])
    info_dict['index'] = i

    # 名字正则化匹配获取
    pat = re.compile(r'/(.*)/(.*?)_0001.jpg')
    name_str = re.search(pat, test_path)
    info_dict['name'] =name_str.group(2)

    # total.append(test_path)
    # true_num_of_pic+=1
    # encoding_temp.append(list(fc.face_encodings(img)[0]))

    random_str = ""
    for j in range(7):
        random_str += random.choice('abcdefghijklmnopqrstuvwxyz_-')
    info_dict['email'] = random_str+"@test.com"

    random_phone = ""
    for j in range(11):
        random_phone += random.choice('1234567890')
    info_dict['phone'] = int(random_phone)

    random_age = random.randrange(18,70)
    info_dict['age'] = random_age

    info_dict['sex'] = random.choice(["male","female"])

    #!! 此处字典必须深拷贝一下，否则total_dict中的字典总在跟随info_dict变化
    total_dict[i] = info_dict.copy()
    print('     done.')






print(total_dict)

# indent参数是json用来格式化字典，好看点，数值为0就直接一行。
json = json.dumps(total_dict,indent=4)
# print(json)
fs = open("./data_pic/2000_face_encoding_v2.json",'w+')
fs.write(json)
fs.close()
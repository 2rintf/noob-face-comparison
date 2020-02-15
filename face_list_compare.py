import face_recognition as fc
import cv2 as cv
import time
import json

test_pic_path = "data_pic/jordan_web_2.jpg"
# img = cv.imread(test_pic_path)
# cv.resize(img,(),)

fs = open("data_pic/1871_pic_list.json",'r+')
pic_dict = json.load(fs)

pic_num = pic_dict['num']
pic_list = pic_dict['path']

distance_list = []
name_list=[]

unknown_image = fc.load_image_file(test_pic_path)
unknown_encoding = fc.face_encodings(unknown_image)[0]
for path_for_compare in pic_list:
    known_image = fc.load_image_file(path_for_compare)
    biden_encoding = fc.face_encodings(known_image)[0]

    distance = fc.face_distance([biden_encoding], unknown_encoding)
    distance_list.append(float(distance))
    name_list.append(path_for_compare)# 后面改成正则提取名字
    print(path_for_compare)
    print("done.")

# 把名字和分数绑成二维数组用于排序
result = zip(name_list,distance_list)
result = [list(i) for i in result]

result_sorted = sorted(result,key=(lambda x: x[1]),reverse=False)
print(result_sorted)
json_data = json.dumps(result_sorted,indent=4)
fs = open("./data_pic/compare_result_"+str(time.ctime()).replace(' ','_')+".json",'w+')
fs.write(json_data)
fs.close()

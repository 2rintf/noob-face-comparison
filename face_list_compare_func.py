import face_recognition as fc
import os
import time
import json


def compare_face_on_json(face_img_path,json_path):
    '''
    此函数将上传的人脸encoding，然后与存储在json文件上的
    已经encoding的人脸进行比较，将结果按欧氏距离从低到高排序，
    存储于新的json文件中。

    :param face_img_path 上传人脸图路径
    :param json_path 人脸encoding数据库文件路径文件
    :return 比较结果json文件的存储路径
            ! 结果文件中有“参与比较的图片路径”与“对应的欧氏距离”

    '''

    try:
        fs = open(json_path, 'r+')
    except OSError:
        return "123"
    pic_dict = json.load(fs)

    pic_num = pic_dict['num']
    pic_list = pic_dict['path']
    pic_encoding_list = pic_dict['encoding']

    distance_list = []
    name_list = []

    counter = 0

    unknown_image = fc.load_image_file(face_img_path)
    unknown_encoding = fc.face_encodings(unknown_image)[0]
    for pic_encoding in pic_encoding_list:
        distance = fc.face_distance([pic_encoding], unknown_encoding)
        distance_list.append(float(distance))
        name_list.append(pic_list[counter])  # 后面改成正则提取名字
        print(pic_list[counter])
        print("done.")
        counter += 1

    # 把名字和分数绑成二维数组用于排序
    result = zip(name_list, distance_list)
    result = [list(i) for i in result]

    result_sorted = sorted(result, key=(lambda x: x[1]), reverse=False)
    print(result_sorted)
    json_data = json.dumps(result_sorted, indent=4)
    save_file_path = "../data_pic/v2_compare_result_" + str(time.ctime()).replace(' ', '_') + ".json"
    fs = open(save_file_path, 'w+')
    fs.write(json_data)
    fs.close()
    return save_file_path


def read_result_from_json():
    '''
    todo:
    读取结果文件，返回排序列表。
    :return:
    '''

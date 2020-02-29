import face_list_compare_func as flcf
import face_recognition as fc
import os
import time
import json
import random
import re

# result = flcf.read_result_from_json("data_pic/v2_compare_result_Fri_Feb_28_18:16:59_2020.json")

# print(result)
#
#
# result[0][0]
#
#
# total_dict = {}
# total_dict[1] = "one"
# print(total_dict)
#
# print(total_dict)


# print(random.choice('abcdefghijklmnopqrstuvwxyz'))
#
# random_str = ""
# random_num = random.randrange(18,70)
# random_s = random.choice(["male","female"])
# for i in range(11):
#     random_str += random.choice('1234567890')
#
# print(int(random_str))
# print(random_num)
# print(random_s)
#
# str = "./data_pic/lfw/Michael_Jordan/Michael_Jordan_0001.jpg"
# pat = re.compile(r'/(.*)/(.*?)_0001.jpg')
# result = re.search(pat,str)
# print(result.group(2))



fs = open("data_pic/3000_face_encoding_v2.json", 'r')

total_dict = json.load(fs)

print(total_dict.__len__())

fs.close()


# print(total_dict['2804'])

print(total_dict["1"].keys())
# for i in range(total_dict.__len__()):
#     print(total_dict[str(i+1)])
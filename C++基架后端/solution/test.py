'''
Descripttion: 
version: 
Author: tylerytr
Date: 2023-09-19 16:43:31
LastEditTime: 2023-09-19 16:44:48
LastEditors: tylerytr
FilePath: /tyleryin/feishu_bot/bagu_bot/src/Interview_experience/C++基架后端/solution/test.py
Email:601576661@qq.com
Copyright (c) 2023 by tyleryin, All Rights Reserved. 
'''
import os
import random

def get_random_file(start_dir):
    # 获取当前文件夹及其子文件夹下的所有文件
    file_list = []
    file_name = ""
    for root, dirs, files in os.walk(start_dir):
        for temp in files:
            #log.info(str(temp))
            file_path = os.path.join(root, temp)
            file_list.append(file_path)
    # file_name=len(file_list)
    if file_list:
        file_name = random.choice(file_list)
    return file_name

# 获取当前文件夹路径
current_dir = os.getcwd()

# 获取随机文件
random_file = get_random_file(current_dir)

if random_file:
    print(f"Randomly selected file: {random_file}")
else:
    print("No files found in the current folder and its subfolders.")
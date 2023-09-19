'''
Descripttion: 
version: 
Author: tylerytr
Date: 2023-09-19 14:33:38
LastEditTime: 2023-09-19 17:04:44
LastEditors: tylerytr
FilePath: /tyleryin/feishu_bot/bagu_bot/src/Interview_experience/C++基架后端/solution/split_files.py
Email:601576661@qq.com
Copyright (c) 2023 by tyleryin, All Rights Reserved. 
'''
import os
import re
def create_files_from_headings(markdown_file):
    with open(markdown_file, "r") as f:
        lines = f.readlines()
        origin_path = os.getcwd()
        origin_path = os.path.join(origin_path,"build")
        path_list=[]
        current_file_name=""
        real_path=""
        count_num=0
        for line in lines:
            # line = line.strip()
            #print(line)
            
            if line.startswith("#"):
                count=line.count("#")
                folder_name = line[count:].strip()
                folder_name = folder_name.replace(' ', '_')
                folder_name = folder_name.replace('/','_')
                if(len(path_list)<count):
                    path_list.append(folder_name)
                else:
                    path_list[count-1]=folder_name
                # 根据path_list 在origin_path后组装文件夹路径
                real_path = origin_path
                for i in range(len(path_list)):
                    real_path = os.path.join(real_path,path_list[i])
                #print(real_path)
                os.makedirs(real_path, exist_ok=True)
                count_num=0
                #print(folder_name)
                # folder_name = folder_name.replace(' ', '_')
                # os.makedirs(folder_name, exist_ok=True)
            else:
                # 检查行是否以整数开头
                if line and line[0].isdigit() :
                    number = line.split('.')[0].strip()
                    #print(line)
                    count_num=count_num+1
                    current_file_name=os.path.join(real_path,str(count_num)+".md")
                    #print(current_file_name)
                    pattern=r'\d+\.'
                    line=re.sub(pattern,"",line)
                    line=line.lstrip()
                    current_file = open(current_file_name, 'w')
                    current_file.write(line)
                    current_file.close()
                    
                elif current_file_name!="":
                    # 在current_file_name中追加写入line
                    current_file = open(current_file_name, 'a')
                    current_file.write(line)
                    current_file.close()
                
                
        
    


if __name__=="__main__":
    # markdown_file = "网络部分答案.md"
    # create_files_from_headings(markdown_file)
    current_directory = os.getcwd()
    # 获取当前目录下所有文件和文件夹的列表
    file_list = os.listdir(current_directory)
    # 筛选出 Markdown 文件
    markdown_files = [file for file in file_list if file.endswith('.md')]
    for file in markdown_files:
        create_files_from_headings(file)




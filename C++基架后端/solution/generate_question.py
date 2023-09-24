'''
Descripttion: 
version: 
Author: tylerytr
Date: 2023-09-24 23:05:44
LastEditTime: 2023-09-24 23:35:42
LastEditors: tylerytr
FilePath: /Interview_experience/C++基架后端/solution/generate_question.py
Email:601576661@qq.com
Copyright (c) 2023 by tyleryin, All Rights Reserved. 
'''
'''
Descripttion: 
version: 
Author: tylerytr
Date: 2023-09-19 14:33:38
LastEditTime: 2023-09-24 23:16:50
LastEditors: tylerytr
FilePath: /Interview_experience/C++基架后端/solution/generate_question.py
Email:601576661@qq.com
Copyright (c) 2023 by tyleryin, All Rights Reserved. 
'''
import os
import re


def generate_question(markdown_file,output_file):
    with open(markdown_file,"r")as f:
        lines = f.readlines()
        file_name = output_file
        print(file_name)
        curremt_file = open(file_name, 'a')
        for line in lines:
            if line.startswith("#") or line[0].isdigit():
                #print(line)
                curremt_file.write(line)
            else:
                test=line.replace(" ","")
                if test[0].isdigit():
                    curremt_file.write(line)
        curremt_file.write("\n")
        curremt_file.close()
                    


if __name__=="__main__":
    # markdown_file = "网络部分答案.md"
    # create_files_from_headings(markdown_file)
    origin_path = "../"
    origin_path = os.path.join(origin_path,"question")
    file_name="面试问题.md"
    file_name = os.path.join(origin_path,file_name)
    file_template_name="question_template"
    file_template_name = os.path.join(origin_path,file_template_name)
    if os.path.exists(file_name):
        os.remove(file_name)    
    #把file_template_name的内容复制到file_name中
    with open(file_template_name,"r")as f_template:
        content=f_template.read()
        #print(content)
        with open(file_name,"w")as f_output:
            f_output.write(content)
        
    
    #print(file_name)

    current_directory = os.getcwd()
    # 获取当前目录下所有文件和文件夹的列表
    file_list = os.listdir(current_directory)
    file_list=sorted(file_list)
    print(file_list)
    # 筛选出 Markdown 文件
    markdown_files = [file for file in file_list if file.endswith('.md')]
    print(markdown_files)
    for file in markdown_files:
        generate_question(file,file_name)




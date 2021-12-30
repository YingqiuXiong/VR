# python3.6                                
# encoding    : utf-8 -*-                            
# @author     : YingqiuXiong
# @e-mail     : 1916728303@qq.com                                    
# @file       : updateid.py
# @Time       : 2021/12/29 11:07
import random

filePath = "review_processingFreWord.txt"
storePath = "review_updateID.txt"
result = open(storePath, "a", encoding="utf-8")
with open(filePath, "r") as f:
    while True:
        line = f.readline()
        if not line:
            break
        line = line.strip("\n").strip("\t").split("\t")
        vr_id = str(random.randint(1000, 9999)) + str(line[0])
        user_id = str(random.randint(1000, 9999)) + str(line[1])
        new_line = vr_id + "\t" + user_id + "\t" + line[2] + "\t" + line[3] + "\n"
        result.write(new_line)
result.close()
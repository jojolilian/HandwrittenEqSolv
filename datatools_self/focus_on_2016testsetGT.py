# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 18:59:09 2020

@author: zqd-d
"""

#focus on the groundtruth.
with open("C:\\Users\\zqd-d\\Desktop\\test2016_groundtruth_Nn.tsv","r")as f2016:
    print(f2016.readlines()[:5])
    
with open("D:\##SelfLernen\PythonPj\接收\model_1_res1000\data\groundtruth_2016.tsv","r")as f2016_old:
    print(f2016_old.readlines()[:5])
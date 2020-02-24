# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 17:21:05 2020

@author: zqd-d
"""

with open("D:\\##SelfLernen\\PythonPj\\接收\\model_1_res1000\\data\\gt_split\\all_new.tsv","r")as f: 
          lines = f.readlines()
#          print(lines)
          with open("D:\\##SelfLernen\\PythonPj\\接收\\model_1_res1000\\data\\gt_split\\all_new.tsv","a")as fw:
             lines = f.readlines()
             for line in lines:
#                 print(line.split())
                 new_line = line.split()
                 new_line.insert(1,'\t')
                 new_line.append('\n')
                 new = ''.join(join)
#                 print(new_line)
                 fw.writelines(new)
                 

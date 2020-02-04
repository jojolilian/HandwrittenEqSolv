# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 23:13:58 2020

@author: zqd-d
"""

with open('./tokens_dl.tsv','r')as f:
    tokens = f.readline().split()
    
    print(len(tokens))
    
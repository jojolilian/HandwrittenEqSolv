# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 23:13:58 2020
Find the number of different symbol types without counting <start><end><pad>
@author: zqd-d
"""

with open('./tokens.tsv','r')as f: #path of tokens.tsv
    tokens = f.readline().split()
    
    print(len(tokens))
    

# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 15:39:21 2020

@author: zqd-d
"""

#new tokens
import nltk
remap = {
        ord('\t'): ' '
        }
remove_t = []
with open("D:\\##SelfLernen\\PythonPj\\接收\\model_1_res1000\\data\\tokens.tsv","r") as ftokens:
          tokens = ftokens.readlines()
          list=[]
#          print(tokenline.translate(remap))
#          print(tokenline.translate(remap).split())
#          print(len(tokenline.translate(remap).split()))
          new= '\t'.join(tokenline.translate(remap).split())
#          print(new)
#          print(type(new))

with open ("D:\\##SelfLernen\\PythonPj\\接收\\model_1_res1000\\data\\tokens_new.tsv","a")as fw:
           fw.write(new)
              
#          for new in tokenline.translate(remap):
#              print(nltk.word_tokenize(new))
#              list = nltk.word_tokenize(new)+list
#        
#          print(len(list))          
          
          
              
              
          
          
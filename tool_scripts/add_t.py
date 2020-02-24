# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 17:21:05 2020

@author: zqd-d
"""

with open("D:\\##SelfLernen\\PythonPj\\接收\\model_1_res1000\\data\\gt_split\\all_new.tsv","r")as f:
          lines = f.readlines()
          print(lines)
#          with open("D:\\##SelfLernen\\PythonPj\\接收\\model_1_res1000\\data\\gt_split\\all_new.tsv","a")as fw:
#             lines = f.readlines()
#             for line in lines:
##                 print(line.split())
#                 new_line = line.split()
#                 new_line.insert(1,'\t')
#                 new_line.append('\n')
#                 new = ''.join(join)
##                 print(new_line)
#                 fw.writelines(new)
                 

##尝试使用list.insert()。insert只会改变当前已经存在的list并且不会 返_回_新_值。list.append('')也是无返回值
##所以不可以用list.insert()的结果赋值给新的变量，该函数没有返回值，如果这里用了赋值语句那这个新list必然空集。
##同时如果不改原list，要先创建待修改list的副本。
                 
#a = 'a sd fw eef wef'
#import nltk
#b = nltk.word_tokenize(a)
#print(b)
##new_b = list(b)
#b.insert(1,'a')  
#print(b)     #klar，测试结果符合预期。
                 
                 
                 
# -*- coding: utf-8  -*     #一个好的编程测试习惯
 
#def main():
#    try:
#        fout = open("test1.txt", "w")
#    except IOError:
#        print "Error: open file failed."
#        return
# 
#    for i in range(5):
#        line = str(i) + "\n"
#        fout.write(line)
# 
#    fout.close()
# 
#if __name__ == "__main__":
#    main()


          
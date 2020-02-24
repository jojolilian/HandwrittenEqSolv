# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 18:39:59 2020

@author: zqd-d
"""

#build bar-diagram

import matplotlib.pyplot as plt
import numpy as np
from dataset_find import load_vocab

tokens_file = "D:\\##SelfLernen\\PythonPj\\接收\\model_1_res1000\\data\\tokens_dl.tsv"
token_to_id, id_to_token = load_vocab(tokens_file)
print(id_to_token)  

#去掉开始结束和pad_tokens
groundtruth_dist = [14, 0, 568, 567, 763, 97, 614, 55, 28, 258, 891, 898, 350, 234, 146, 116, 108, 103, 104, 520, 40, 35, 36, 21, 24, 13, 15, 10, 23, 15, 20, 16, 28, 24, 15, 15, 37, 17, 50, 0, 0, 6, 55, 42, 0, 0, 77, 18, 2, 3, 505, 14, 21, 9, 4, 52, 81, 5, 34, 40, 33, 31, 0, 36, 16, 14, 7, 16, 13, 74, 22, 13, 40, 43, 8, 98, 242, 79, 40, 79, 82, 0, 11, 11, 50, 884, 981, 342, 223, 132, 154, 66, 95, 46, 40, 132, 43, 90, 22, 67, 307, 12, 84, 44, 72, 35, 95, 47, 41, 20, 695, 247, 153, 1843, 66, 1843]
eva = [2, 0, 637, 645, 817, 45, 580, 19, 16, 183, 795, 904, 363, 180, 149, 64, 73, 55, 64, 545, 18, 11, 15, 13, 34, 1, 3, 1, 0, 3, 1, 4, 1, 2, 5, 9, 27, 5, 20, 1, 2, 0, 25, 43, 4, 2, 73, 0, 0, 0, 531, 1, 7, 0, 0, 53, 55, 0, 9, 89, 21, 33, 6, 18, 10, 74, 0, 8, 0, 43, 5, 1, 43, 7, 3, 88, 248, 67, 37, 68, 42, 28, 2, 0, 12, 823, 635, 250, 166, 80, 118, 51, 109, 85, 36, 53, 7, 56, 1, 69, 309, 4, 80, 18, 26, 23, 97, 24, 15, 3, 911, 318, 119, 2516, 17, 2386]

#find the result with non symbol tokens
non_symbols = [
    "{",
    "}",
    "\\left",
    "\\right",
    "_",
    "^",
    "\\Big",
    "\\Bigg",
    "\\limits",
    "\\mbox",
]

id_n_sy = [token_to_id[n_sy] for n_sy in non_symbols]
#print(id_n_sy)     #ids of non symbol tokens

extract_nsy_gt = [groundtruth_dist[i] for i in id_n_sy]
#print(extract_nsy_gt)      #appearance times of non symbol tokens in groundtruth(2016testset)
extract_nsy_eva = [eva[i] for i in id_n_sy]
#print(extract_nsy_eva)     #appearance times of non symbol tokens in prediction



#general plot
size = len(groundtruth_dist)
x = np.arange(size)
a = groundtruth_dist
b = eva


total_width, n = 0.8,2
width = total_width / n
x = x - (total_width - width) / 2

plt.barh(x, a,  label='groundtruth_dist')
plt.barh(x + width, b, label='eva')
#plt.bar(range(len(groundtruth_dist)),groundtruth_dist)
#plt.bar(range(len(eva)),eva)
plt.legend()
plt.show()

#focus on non symbol tokens

c = np.array(extract_nsy_gt)
d = np.array(extract_nsy_eva)
#print(c)

plt.barh(range(len(c)), c,label='extract_nsy_gt',tick_label=non_symbols)
plt.barh(range(len(d)), -d, label='extract_nsy_eva')
plt.legend()
plt.show()


#focus on \frac, a , u, 





#find most different tokens' accounts and return its id.
def get_key(dict,value):
    
    return [k for k,v in dict.items() if v==value]

def get_mostdiff_tokens_ids(comp_list_a,comp_list_b,num):
    
    compar = []
    for i, token_times in enumerate(comp_list_a):
        compar.append(comp_list_a[i] - comp_list_b[i])
    
#print(compar)
    compar_result = enumerate(compar)
    compar_dict = dict(compar_result)

    most_dif_times = sorted(compar, key=abs)[-num:]
    most_dif_tokens = []


    for i in most_dif_times:
        most_dif_tokens.append(get_key(compar_dict,i))

    most_dif_tokens = [ii for [ii] in most_dif_tokens]
    return(most_dif_tokens,most_dif_times)
#print(most_dif_tokens)
    
    
#print(get_mostdiff_tokens_ids(groundtruth_dist,eva,10))

token_in_list, most_dif_times= get_mostdiff_tokens_ids(groundtruth_dist,eva,10)
print(token_in_list)
#most_dif_token = [i for [i] in token_in_list ]
#print(most_dif_token)

plt.bar(range(len(most_dif_token)), most_dif_times,tick_label=most_dif_token)
plt.show()

    
    


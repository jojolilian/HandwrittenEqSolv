# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 18:39:59 2020

@author: zqd-d
"""

#build bar-diagram
#import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from dataset_find import load_vocab

tokens_file = "D:\\##SelfLernen\\PythonPj\\接收\\model_1_res1000\\data\\tokens.tsv"  #path of tokens.tsv(tokens dictionary)
token_to_id, id_to_token = load_vocab(tokens_file)
#print(id_to_token)  


#remove start-, end- and pad-tokens
groundtruth_dist = [14, 0, 568, 567, 763, 97, 614, 55, 28, 258, 891, 898, 350, 234, 146, 116, 108, 103, 104, 520, 40, 35, 36, 21, 24, 13, 15, 10, 23, 15, 20, 16, 28, 24, 15, 15, 37, 17, 50, 0, 0, 6, 55, 42, 0, 0, 77, 18, 2, 3, 505, 14, 21, 9, 4, 52, 81, 5, 34, 40, 33, 31, 0, 36, 16, 14, 7, 16, 13, 74, 22, 13, 40, 43, 8, 98, 242, 79, 40, 79, 82, 0, 11, 11, 50, 884, 981, 342, 223, 132, 154, 66, 95, 46, 40, 132, 43, 90, 22, 67, 307, 12, 84, 44, 72, 35, 95, 47, 41, 20, 695, 247, 153, 1843, 66, 1843]
#print(len(groundtruth_dist))
eva_litdata = [2, 0, 630, 650, 805, 46, 568, 18, 14, 178, 781, 900, 342, 171, 145, 62, 76, 54, 60, 527, 16, 10, 12, 12, 30, 0, 3, 1, 0, 2, 0, 2, 1, 2, 5, 7, 24, 5, 18, 0, 0, 0, 26, 41, 5, 2, 75, 0, 0, 0, 522, 1, 7, 0, 0, 47, 51, 0, 10, 83, 20, 30, 7, 20, 6, 92, 0, 6, 0, 44, 5, 1, 40, 8, 3, 81, 253, 65, 34, 60, 40, 27, 0, 0, 13, 810, 629, 246, 163, 75, 119, 51, 108, 74, 30, 51, 6, 52, 1, 56, 300, 3, 80, 21, 27, 24, 95, 22, 16, 3, 896, 318, 106, 2569, 18, 2299]
#eva_litdata:evaluation result of the 'with 128*128 sized plot' original trained weight.


eva113_most = [5, 0, 554, 598, 791, 73, 562, 25, 0, 233, 802, 1060, 313, 209, 193, 118, 73, 87, 72, 529, 37, 24, 15, 17, 22, 6, 10, 6, 13, 2, 7, 1, 13, 13, 4, 9, 36, 4, 16, 0, 1, 0, 29, 57, 2, 1, 76, 4, 0, 2, 500, 4, 21, 0, 0, 50, 58, 0, 17, 29, 35, 30, 1, 23, 6, 32, 0, 16, 4, 45, 10, 3, 8, 23, 2, 106, 217, 82, 37, 64, 72, 15, 0, 1, 13, 811, 719, 321, 198, 114, 140, 48, 83, 65, 25, 96, 20, 103, 1, 51, 310, 1, 93, 36, 22, 39, 81, 36, 23, 8, 728, 303, 119, 2071, 42, 1881]
#eva113_most:evaluation result of the' with 256(higher resolution)mostdata' trained weight.

eva124_most3CNN = [12, 0, 644, 605, 746, 76, 581, 35, 0, 237, 824, 935, 370, 197, 135, 110, 68, 93, 81, 550, 33, 39, 10, 16, 19, 2, 6, 2, 8, 1, 4, 4, 13, 9, 7, 2, 38, 9, 22, 0, 2, 1, 36, 31, 3, 5, 78, 4, 0, 2, 510, 3, 19, 4, 3, 54, 71, 0, 15, 56, 28, 33, 4, 27, 9, 40, 0, 12, 3, 73, 6, 6, 24, 16, 2, 87, 219, 80, 32, 60, 78, 18, 1, 0, 6, 760, 698, 318, 164, 142, 153, 45, 96, 51, 31, 92, 14, 70, 5, 69, 347, 0, 92, 25, 23, 20, 127, 48, 25, 5, 689, 288, 116, 2114, 34, 1969]
#eva124_most3CNN:evaluation result of the 'with 256(higher resolution)mostdata and improved model ' trained weight.




#find the result with non symbol tokens
non_symbols = [  
    "_",
    "^",
    "\\frac",
    "\\left",
    "\\mbox",
    "\\right"
]

id_n_sy = [token_to_id[n_sy] for n_sy in non_symbols]
#print(id_n_sy)     #ids of non symbol tokens

extract_nsy_gt = [groundtruth_dist[i] for i in id_n_sy]
#print(extract_nsy_gt)      #appearance times of non symbol tokens in groundtruth(2016testset)


################################################################################################################

extract_nsy_eva_litdata  = [eva_litdata [i] for i in id_n_sy]
#print(extract_nsy_eva)     #appearance times of non symbol tokens in prediction

extract_nsy_eva113_most = [eva113_most[i] for i in id_n_sy]
#appearance times of non symbol tokens in prediction eva256

extract_nsy_eva124_most3CNN = [eva124_most3CNN[i] for i in id_n_sy]
#appearance times of non symbol tokens in prediction eva124


##focus on non symbol tokens including \frac

c = np.array(extract_nsy_gt)
d = np.array(extract_nsy_eva_litdata)
#print(c)

plt.barh(range(len(c)), c,label='extract_nsy_gt',tick_label=non_symbols)
plt.barh(range(len(d)), -d, label='extract_nsy_eva_litdata')
plt.legend()
plt.show()


e = np.array(extract_nsy_eva113_most)
plt.barh(range(len(c)), c,label='extract_nsy_gt',tick_label=non_symbols)
plt.barh(range(len(d)), -e, label='extract_nsy_eva113_most')
plt.legend()
plt.show()


f = np.array(extract_nsy_eva124_most3CNN)
plt.barh(range(len(c)), c,label='extract_nsy_gt',tick_label=non_symbols)
plt.barh(range(len(d)), -f, label='extract_nsy_eva124_most3CNN')
plt.legend()
plt.show()

######################################################################################################


#find most different tokens' accounts and return its id.
def get_key(dict,value):
    
    return [k for k,v in dict.items() if v==value]

def get_mostdiff_tokens_ids(comp_list_a,comp_list_b,num):
    
    compar = []
    for i, token_times in enumerate(comp_list_a):
        
        compar.append(comp_list_a[i] - comp_list_b[i])
    

    compar_result = enumerate(compar)
    compar_dict = dict(compar_result) #give every result a number

    most_dif_times = sorted(compar, key=abs)[-num:]
    most_dif_tokens_ids = []


    for i in most_dif_times:
        most_dif_tokens_ids.append(get_key(compar_dict,i))  #the perspective different occuring times

    most_dif_tokens_ids = [ii for [ii] in most_dif_tokens_ids]
    return(most_dif_tokens_ids,most_dif_times)
    
#print(most_dif_tokens)
def flat(nums):
    res = []
    for i in nums:
        if isinstance(i, list):
            res.extend(flat(i))
        else:
            res.append(i)
    return res    

def relativ_dist(comp_list_a,comp_list_b,num):
#    comp_list_a,comp_list_b=groundtruth_dist,eva256
#    num = 10
    compar = []
#    missing_ids = []
#    missing_words_times = []
#    for i, token_times in enumerate(comp_list_a):
#        if comp_list_a[i]!=0 and comp_list_b[i]==0 :
#            missing_words_times.append(comp_list_a[i])
#            missing_ids = [i]
#            
#    missing_words = [token_to_id[i] for i in missing_ids]
#    print(missing_words)
    for i,token_times in enumerate(comp_list_a):
        if comp_list_a[i]==0 : 
#        if comp_list_a[i]==0 or comp_list_b[i]==0 or comp_list_b[i]==1: #remove the missing or total wrongly ocurr tokens
#            compar.append((comp_list_a[i] - comp_list_b[i])/1)
            compar.append(0)
        else:
            compar.append((comp_list_a[i] - comp_list_b[i])/comp_list_a[i])
#    print(compar)
    compar_result = enumerate(compar)
    compar_dict = dict(compar_result)
#    print(compar_dict.items())

#    print(compar_dict[2]) 

    rltv_times = sorted(compar, key=abs,reverse=True)[:num]
    
    rltv_ids = []
#    print(rltv_times)
    for i in rltv_times:
        
        if len(get_key(compar_dict,i))>1 :
            for ii in range(len(get_key(compar_dict,i))):
                rltv_ids.append(get_key(compar_dict,i)[ii])
        
        else:
            rltv_ids.append(get_key(compar_dict,i)[0]) 
                    
        
    
    
#    print(rltv_ids)
    

    new_ids = sorted(set(rltv_ids),key=rltv_ids.index)
#    print(new_ids)
    rltv_ids=new_ids[:num]
#    print(rltv_ids)
#    print(new_ids.index) #method object
    

    
    
    return (rltv_ids,rltv_times)
    
##################################################################################################################
#print(get_mostdiff_tokens_ids(groundtruth_dist,eva,10))



#eva_litdata/eva113_most/eva124_most3CNN

#==========relative different tokens of 128 original model==========
rltv_ids,rltv_times=relativ_dist(groundtruth_dist,eva_litdata,20)
rltv_dif_tokens = [id_to_token[i] for i in rltv_ids]
print(rltv_dif_tokens) #x-axis of the grafik


plt.rcParams['figure.figsize'] = (13.0, 3.0)    
plt.bar(range(len(rltv_dif_tokens)), rltv_times,tick_label=rltv_dif_tokens)
    
for (a,b) in zip(range(len(rltv_dif_tokens)),rltv_times):
    plt.text(a, b, '%.2f' % b, ha='center', va= 'bottom',fontsize=11)
plt.show()   


#==============relative different tokens of the' with 256(higher resolution)mostdata'trained model================

rltv_ids_256_more,rltv_times_256_more=relativ_dist(groundtruth_dist,eva113_most,20)
rltv_dif_tokens_256_more = [id_to_token[i] for i in rltv_ids_256_more]
print(rltv_dif_tokens_256_more)



plt.rcParams['figure.figsize'] = (13.0, 3.0)    
plt.bar(range(len(rltv_dif_tokens_256_more)), rltv_times_256_more,tick_label=rltv_dif_tokens_256_more)
for (a,b) in zip(range(len(rltv_dif_tokens_256_more)),rltv_times_256_more) :
    plt.text(a, b, '%.2f' % b, ha='center', va= 'bottom',fontsize=11)
    
plt.show()

#==============relative different tokens of the' with 256(higher resolution)mostdata and 3cnn structure'trained model================

rltv_ids_256_3cnn,rltv_times_256_3cnn=relativ_dist(groundtruth_dist,eva124_most3CNN,20)
rltv_dif_tokens_256_3cnn = [id_to_token[i] for i in rltv_ids_256_3cnn]
print(rltv_dif_tokens_256_3cnn)
plt.rcParams['figure.figsize'] = (13.0, 3.0)    
plt.bar(range(len(rltv_dif_tokens_256_3cnn)), rltv_times_256_3cnn,tick_label=rltv_dif_tokens_256_3cnn)
for (a,b) in zip(range(len(rltv_dif_tokens_256_3cnn)),rltv_times_256_3cnn) :
    plt.text(a, b, '%.2f' % b, ha='center', va= 'bottom',fontsize=11)
    
plt.show()














#tools bar
#def get_occurance_gt(list,gt): #没有用
#    dist_in_gt=[]
#    for t in list:
#        dist_in_gt.append(gt[id_to_token(t)]) #没有用
#    return dist_in_gt
#
#def get_occurance_tr(list,tr):
#    dist_in_train=[]
#    for t in list:
#        dist_in_train.append(tr[id_to_token(t)])
#    return dist_in_train


        
    

#plt.figure(dpi=300)
#x = length_pred_distribute[0]
#x = np.array(x)
#y = actual_distribute[0]
#y = np.array(y)
#
#
#label = [x for x in range (100)]
#label_space = [x for x in range (-10,990,10)]
#
#ax = plt.gca()
#tick_spacing = 10
#plt.title('Comparation of recognized and true expressions')
#plt.xlabel('Length(Number of all tokens)')
#plt.ylabel('Count of expression')
#plt.bar(label,x,tick_label = label_space,label = 'Recognition',alpha = 0.5)
#plt.bar(label,y,tick_label = label_space,label = 'Truth',alpha = 0.5)
#ax.legend()
#ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))

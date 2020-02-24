# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 22:17:28 2020

@author: zqd-d
"""

from dataset_find import CrohmeDataset,collate_batch
from torchvision import transforms
import os.path


groundtruth_file = "C:\\Users\\zqd-d\\Desktop\\test2016_groundtruth_Nn.tsv"
#待转化成id的文件

tokensfile = "D:\\##SelfLernen\\PythonPj\\接收\\model_1_res1000\\data\\tokens_dl.tsv"
#字典
root = "C:\\Users\\zqd-d\\Desktop\\train\\"
#相对路径



input_size = (256, 256)




transformers = transforms.Compose(
    [
        # Resize so all images have the same size
        transforms.Resize(input_size),
        transforms.ToTensor(),
    ]
)

train_dataset = CrohmeDataset(
        groundtruth_file, tokensfile,  root=root,transform=transformers
    )#crop=options.crop,

#print(train_dataset.__dict__)


##这里要整一个token_to_id出来：
#
#token_to_id,id_to_token = load_vocab(tokensfile)
#
#
#
##encode ground truth成list们并且写出来（带名和不带名）：
#
#with open(groundtruth_file,"r")as f_gt:
#    gt_lines = f_gt.readlines()
#    with open(os.path.dirname(groundtruth_file)+"\\ids.tsv","a")as fid:
#        
#        for gt_line in gt_lines:    #gt_line has its file name
#            row = gt_line.split("\t",1)
#            ids = encode_truth(row[1],token_to_id)
#            fid.writelines(ids)
 
#print(collate_batch(train_dataset.data)) 
ids_dist = [0 for i in range(119)]
with open(os.path.dirname(groundtruth_file)+"\\ids_2016test_dl.tsv","w")as fid:  
    fid.write("#############___HERE_ARE_IDS_OF_SEQ_IN_2016TESTSET___#############")
    fid.write("\n")
    for data in train_dataset.data:
#        print(data["truth"]["encoded"])
        fid.write(str(data["truth"]["encoded"]))
        fid.write('\n')
        for i in data["truth"]["encoded"]:
                ids_dist[i]+=1
#        print(ids_dist)
        

        

        
        

        

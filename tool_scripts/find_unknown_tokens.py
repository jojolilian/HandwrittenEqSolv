# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 23:22:57 2020

@author: zqd-d
"""

from dataset_find import CrohmeDataset
from torchvision import transforms

gt_train = "C:\\Users\\zqd-d\\Desktop\\test2016_groundtruth.tsv"  #path of the file containing groundtruth to be checked

tokensfile = "D:\\##SelfLernen\\PythonPj\\接收\\model_1_res1000\\data\\tokens_new.tsv" # path of tokens.tsv (token dictionary)
root = "C:\\Users\\zqd-d\\Desktop\\train\\"



input_size = (256, 256)




transformers = transforms.Compose(
    [
        # Resize so all images have the same size
        transforms.Resize(input_size),
        transforms.ToTensor(),
    ]
)

train_dataset = CrohmeDataset(
        gt_train, tokensfile,  root=root,transform=transformers
    )#crop=options.crop,

#if the code could run, it means all training data is correctly packaged.



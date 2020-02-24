In this folder there should be some subfolders:
gt_split, random splited groundtruth_train.tsv in data into 'validation_new.tsv' and 'train_new.tsv'by using train_validation_split.py in 'data_tools'
test, contains a folder named 2016 which includes pngs of 2016 testset in the size of 256*256
train, contains all and only pngs of trainset(11046), by decompressing the data.zip in the 'train' folder.


and also some .tsv files:
tokens.tsv, symbol dictionary which contains all types of single symbol.(119 tokens with prensent training data)
groundtruth_train.tsv, groundtruth_2016.tsv

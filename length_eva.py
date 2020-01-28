"""
    this programm is to count the number of the tokens in the predicted seq
    evaluate the distributions of 3 diffrent statistic data
    1 expected length
    2 actual length
    3 distance between 1 & 2
"""
from dataset import load_vocab
#import re
to2id , id2to = load_vocab('./data/tokens.tsv')
print(id2to)

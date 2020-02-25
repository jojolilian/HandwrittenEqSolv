from dataset import load_vocab
#import re
to2id , id2to = load_vocab('./data/tokens.tsv')
f_wrong = open('./after_beam_search.txt','r')

f_wrong_processing = open('./after_beam_search_converted.txt','a')

for line in f_wrong:
    out = []
    line = line.replace("\n", "")
    line = line.replace("]", "\n")
    line = line.replace(",", "")
    line = line.replace("[", "[ ")
    line = line.replace(")", "")
    line = line.split()
    [out.append(id2to[int(num)].strip("'")) if num.isdigit() else out.append(num.strip("'")) for num in line]
    q = "".join(out)
    q = q.replace('[[','[')
    q = q.replace("tensor(", "\n") 
    q = q.replace("[", "\n")
    q = q.replace("<PAD>", "")
    q = q.replace("<EOS>", "") 
    q = q.replace("<SOS>",'')
    f_wrong_processing.write(str(q))
f_wrong.close()
f_wrong_processing.close()
print('convert finished!')      

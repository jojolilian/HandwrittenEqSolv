f_in = open('./groundtruth_train.tsv','r')
f_out = open('./groundtruth_train_no_root','a')
for i in f_in:
    i = i.split('/')
    m = ''.join(i[1:])
    print(m)
    f_out.write(str(m))


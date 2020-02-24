
#import csv
#####目的为转变data label格式  输入源datalabel的路径label_file，和生成转换后label的路径new_label_file
def label_conv(label_file,new_label_file):

    fp2=open(label_file,'r')
#    labels = csv.reader(fp2)
    labels=fp2.readlines()
    fp2.close()
    final_label = []
#
    for n,l in enumerate(labels):

        if l == '"':
            continue            #####我加的 为了去除 label文件中无用的   "
        #        tmp=l.strip().split(' ',1)#        uid=tmp[0]
        tmp=l.strip().split()[1:]
        route=l.strip().split()[0]
        t=''.join(tmp)
        leerstr = ' '
        print('原句：'+l)
        for letter in t:
            if letter != ' ':
                leerstr = leerstr + str(letter)+' '
            else:
                leerstr = leerstr + str(letter)
        leerstr = leerstr.replace(" \ ", "  \ ")    
        leerstr = leerstr.replace(" \ B i g g ", " \Bigg ")
        leerstr = leerstr.replace(" \ B i g ", " \Big ")
        leerstr = leerstr.replace('"', '')
        leerstr = leerstr.replace(" \ D e l t a ", " \Delta ")
        leerstr = leerstr.replace(" \ a l p h a ", " \\alpha ")
        leerstr = leerstr.replace(" \ b e t a ", " \\beta ")
        leerstr = leerstr.replace(" \ c d o t s ",  " \cdots ")
        leerstr = leerstr.replace(" \ c d o t ", " \cdot ")

        leerstr = leerstr.replace(" \ c o s ",  " \cos ")
        leerstr = leerstr.replace(" \ d i v ", " \div ")
        leerstr = leerstr.replace(" \ e x i s t s ", " \exists ")
        leerstr = leerstr.replace(" \ f o r a l l ", " \\forall ")
        leerstr = leerstr.replace(" \ f r a c ", " \\frac ")
        leerstr = leerstr.replace(" \ g a m m a ", " \gamma ")
        leerstr = leerstr.replace(" \ g e q ", " \geq ")
        leerstr = leerstr.replace(" \ g t ", " \gt ")

        leerstr = leerstr.replace(" \ i n f t y ",  " \infty ")
        leerstr = leerstr.replace(" \ i n t ", " \int ")
        leerstr = leerstr.replace(" \ l a m b d a ", " \lambda ")
        leerstr = leerstr.replace(" \ l d o t s ", " \ldots ")
        leerstr = leerstr.replace(" \ l e f t ", " \left ")
        leerstr = leerstr.replace(" \ l e q ", " \leq ")

        leerstr = leerstr.replace(" \ l i m i t s ", " \limits ")
        leerstr = leerstr.replace(" \ l i m ", " \lim ")
        leerstr = leerstr.replace(" \ l o g ", " \log ")
        leerstr = leerstr.replace(" \ l t ", " \lt ")
        leerstr = leerstr.replace(" \ m b o x ", " \mbox ")
        leerstr = leerstr.replace(" \ n e q ", " \\neq ")
        leerstr = leerstr.replace(" \ m u ", " \mu ")
        leerstr = leerstr.replace(" \ p h i ", " \phi ")
        leerstr = leerstr.replace(" \ p i ", " \pi ")
        leerstr = leerstr.replace(" \ p m ", " \pm ")
        leerstr = leerstr.replace(" \ p r i m e ", " \prime ")
        leerstr = leerstr.replace(" \ r i g h t a r r o w ", " \\rightarrow ")
        leerstr = leerstr.replace(" \ r i g h t ", " \\right ")
        leerstr = leerstr.replace(" \ s i g m a ", " \sigma ")
        leerstr = leerstr.replace(" \ s i n ", " \sin ")
        leerstr = leerstr.replace(" \ s q r t ", " \sqrt ")
        leerstr = leerstr.replace(" \ s u m ", " \sum ")
        leerstr = leerstr.replace(" \ t a n ", " \\tan ")
        leerstr = leerstr.replace(" \ t h e t a ", " \\theta ")
        leerstr = leerstr.replace(" \ t i m e s ", " \\times ")
        leerstr = leerstr.replace(" \ t o ", " \\to ")
        leerstr = leerstr.replace(" \ i n ", " \in ")
        leerstr = leerstr.replace(" \ { ", " \{ ")
        leerstr = leerstr.replace(" \ } ", " \} ")
        
        
        
        
        
#'''
#these conversion is for the crohme testingsets of 2013,2014,2016
#'''
        leerstr = leerstr.replace(" < ", " \\lt ")
        leerstr = leerstr.replace(" > ", " \\gt ")
            # Remove \mathrm and \vtop are only present in the test sets, but not in the
    # training set. They are purely for formatting anyway.
        leerstr = leerstr.replace(" \ m a t h r m ", " ")
        leerstr = leerstr.replace(" \ v t o p ", " ")
        # \; \! are spaces and only present in 2014's test set
        leerstr = leerstr.replace(" \ ; ", " ")
        leerstr = leerstr.replace(" \ ! ", " ")
#        leerstr = leerstr.replace(" \ ", " ")
        # There's one occurrence of \dots in the 2013 test set, but it wasn't present in the
        # training set. It's either \ldots or \cdots in math mode, which are essentially
        # equivalent.
        leerstr = leerstr.replace(" \ d o t s ", " \\ldots ")
        # Again, \lbrack and \rbrack where not present in the training set, but they render
        # similar to \left[ and \right] respectively.
        leerstr = leerstr.replace(" \ l b r a c k ", " [ ")
        leerstr = leerstr.replace(" \ r b r a c k ", " ] ")
        # Same story, where \mbox = \leavemode\hbox
        leerstr = leerstr.replace(" \ h b o x ", " \\mbox ")
        # There is no reason to use \lt or \gt instead of < and > in math mode. But the
        # training set does. They are not even LaTeX control sequences but are used in
        # MathJax (to prevent code injection).
        # \parallel renders to two vertical bars
        leerstr = leerstr.replace(" \ p a r a l l e l ", " | | ")
        # Some capital letters are not in the training set...
        leerstr = leerstr.replace(" O ", " o ")
        leerstr = leerstr.replace(" W ", " w ")
        leerstr = leerstr.replace(" \ P i ", " \pi ")
            
        
        
        
        
        
        
        
        
        
        
        
        
        final_item = route +'       '+ leerstr
        final_label.append(final_item)
        print('处理后：'+final_item)
        print(n)
    with open(new_label_file,"w") as f:
        for i in final_label:
            f.write(str(i)+'\n')
        f.close()

label_file = './test_from_model1/groundtruth_2016.tsv'#'./train_from_model1/groundtruth_train.tsv'
new_label_file = 'test_caption_2016.txt'
label_conv(label_file,new_label_file)    
# id2to.py
This script is to transfer the raw output of neuron network into readable expressions using the dictionary. It convert the number to the token which the number represents.



# label_conv_try.py
This script is used to unify the format of the label of two different label file. 
At the begining of the project, we compared two different models. To get a fair result, we have to train two different models on the same dataset. This script transforms the label file and enables the training of two models on a same data set.



# plot_stats_length.py
This script is used to plot the analyse result of sequence analysis. Details can be seen in the README.md in the root.


# find_missing_label.py
This script is used to compare between the number of all handwritten plots and the number of groundtruth.

# dataset_find.py
This script is a function source which is refered by 'find_unknown_tokens.py'to find the unknown tokens.

# find_unknown_tokens.py
This script is used to find unknown tokens, when there occurs an unknown token ,it excepts and give a message of the place of the unknown token in the groundtruth file

# plt_bar_diagram.py
This script figure out the relative different tokens and plot them with different evaluated results. Also plot the distribution of most-common-different-predicted tokens between the groundtruth and the prediction.



# Handwritten Equation Solver

Based on Multi-Scale Attention with Dense Encoder for Handwritten Mathematical Expression Recognition.

## table of content
- [Requirements](#requirements)
- [Data](#data)
- [Usage](#usage)
  * [Training](#training)
  * [Evaluating](#evaluating)
  * [Ploting](#ploting)
- [Related Efforts](#related-efforts)
## Requirements

Python 3
PyTorch

All dependencies can be installed with PIP.

`pip install -r requirements.txt`

If you'd like to use a different installation method or another CUDA version with PyTorch (e.g. CUDA 10) follow the instructions on PyTorch - Getting Started.

## Data

CROHME Competition on Recognition of Offline Handwritten Mathematical Expressionse 
Dataset source: http://tc11.cvc.uab.es/datasets/ICFHR-CROHME-2016_1


## Usage
### Training
There are totally 3 different models. 
1. Recognize the images with resolution of 128*128
2. Recognize the images with resolution of 256*256
3. Recognize the images with resolution of 256*256(model with deeper CNNs) 
To implement the training precess there are 3 defferent options(3 corresponding different .py files).

And we also provide the best weights of these three different models in the /checkpoints file.

For example you can procced the training of our best model weight by inputing the command in the terminal below:

`python train_256.py --prefix "name_you_want" -n 200 -c checkpoints/res256_tr_mostdata_3_0113.pth`

Or you can also start a new one by:

`python train_256.py --prefix "name_you_want" -n 200`

For all options see 

`python train.py --help:`

### Evaluating
The `evaluate.py` contains both predicting and evaluating process. Since there are 3 different models, the evaluating part has also 3 different files. For each different models we also did some analysis(sequence and token) on the result and by running the `evaluate.py`, we shall get the statistical count of the predictions, and these statistical result will be presented in form of histogramm in later works.

For example: to evaluate the model with deeper CNNs use the `evaluate.py` script with the best weight we got on the test set 2016 and the beam width of 5:

`python evaluate_256_3CNNs.py -d 2016 --beam-width 5 -c checkpoints/3CNN_tr_mostdata0124.pth`

Different evaluation.py and there corresponding model.py:
evaluate_old_128.py  -> model_old_128.py
evaluate_new_256.py  -> model.py
evaluate_256_3CNNs.py-> model_3CNNs.py

### Ploting
The results from the evaluating part contains all the statical counts of both sequence and token analysis. And by using these result we can show the result in plots and find out the problems in the model easier.

After copying the data into the `plot_stats_length.py` , we can easily get the plots of sequence analysis by running the command below in the terminal.
`python plot_stats_length.py`

## Related Efforts
* [jungomi/math-formula-recognition](https://github.com/jungomi/math-formula-recognition)
* [whywhs/Pytorch-Handwritten-Mathematical-Expression-Recognition](https://github.com/whywhs/Pytorch-Handwritten-Mathematical-Expression-Recognition)

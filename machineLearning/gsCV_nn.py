import scipy.io
import numpy as np
import matplotlib.pyplot as plt
from loadData import loadData
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import confusion_matrix

######################### LOAD DATA ##############################################
testF = 'dp210'
trainF = ['5pourcent/dataset145_a']
inj_Xtr, load_Xtr, gen_Xtr, secuN_Ytr, xte, secuN_Yte = loadData(testF, trainF)
xtr = [ inj_Xtr, load_Xtr, gen_Xtr]

######################### GLOBAL SETTINGS #######################################
#param_grid = { 'alpha': np.arange(0.00001, 0.001, 0.0001) }
param_grid = { 'alpha': np.arange( 0.000090, 0.00011, 0.000001) }
#model = GridSearchCV( MLPClassifier(), param_grid, cv=5)
model  = [ MLPClassifier(hidden_layer_sizes=(120,)),
           MLPClassifier(hidden_layer_sizes=(100,)),
           MLPClassifier(hidden_layer_sizes=(130,))]
           
######################### MACHINE LEARNING #######################################
for Fe in [0,2]: # all kind of features
    print('fiting...')
    model[Fe].fit( xtr[Fe], secuN_Ytr.ravel()) # grid search CV
    if Fe == 0: typeF = 'Injected'
    elif Fe == 1: typeF = 'Load'
    else: typeF = 'Gen'
    print(confusion_matrix( secuN_Ytr, model[Fe].predict(xtr[Fe])))
#    print( typeF, 'best : ', model.best_params_)
   
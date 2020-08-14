import scipy.io
import numpy as np
from loadData import loadData
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV

######################### LOAD DATA ##############################################
testF = 'dp210'
trainF = ['5pourcent/dataset145_a']
inj_Xtr, load_Xtr, gen_Xtr, secuN_Ytr, xte, secuN_Yte = loadData(testF, trainF)
xtr = [ inj_Xtr, load_Xtr, gen_Xtr]

######################### GLOBAL SETTINGS #######################################
data_sampling = 96 # 96 value for one day (1/4 d'heure)
param_grid0 = { 'C' : np.arange(500, 510 , 1) }
param_grid1 = { 'C' : np.arange(7.5, 7.8, 0.1) }
param_grid2 = { 'C' : [1e-50,1e-30,1e-20,1e-12]}
#                'kernel' : ['linear', 'poly', 'rbf', 'sigmoid', 'precomputed'],
#                'degree' : np.arange(1, 6, 1),
#                'gamma' : ['scale', 'auto'] }
model = [ GridSearchCV( SVC(), param_grid0, cv=5),
          GridSearchCV( SVC(), param_grid1, cv=5),
          GridSearchCV( SVC(), param_grid2, cv=5)]
           
######################### MACHINE LEARNING #######################################
for Fe in [0]: # all kind of features
    print('fiting ...')
    model[Fe].fit( xtr[Fe], secuN_Ytr.ravel()) # grid search CV
    if Fe == 0: typeF = 'Injected'
    elif Fe == 1: typeF = 'Load'
    else: typeF = 'Gen'
    print( typeF, 'best : ', model[Fe].best_params_)
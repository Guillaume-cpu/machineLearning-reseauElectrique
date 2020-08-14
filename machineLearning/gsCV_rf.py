import scipy.io
import numpy as np
from loadData import loadData
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

######################### LOAD DATA ##############################################
testF = 'dp210'
trainF = ['5pourcent/dataset145_a']
inj_Xtr, load_Xtr, gen_Xtr, secuN_Ytr, xte, secuN_Yte = loadData(testF, trainF)
xtr = [ inj_Xtr, load_Xtr, gen_Xtr]

######################### GLOBAL SETTINGS #######################################
param_grid0 = { 'n_estimators': np.arange(64, 67, 1) }
param_grid1 = { 'n_estimators': np.arange(82, 85, 1) }
param_grid2 = { 'n_estimators': np.arange(50, 53, 1) }
model = [ GridSearchCV( RandomForestClassifier(), param_grid0, cv=5),
          GridSearchCV( RandomForestClassifier(), param_grid1, cv=5),
          GridSearchCV( RandomForestClassifier(), param_grid2, cv=5)]
           
######################### MACHINE LEARNING #######################################
for Fe in range(3): # all kind of features
    print('fiting...')
    model[Fe].fit( xtr[Fe], secuN_Ytr.ravel()) # grid search CV
    if Fe == 0: typeF = 'Injected'
    elif Fe == 1: typeF = 'Load'
    else: typeF = 'Gen'
    print( typeF, 'best : ', model[Fe].best_params_)
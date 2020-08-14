import numpy as np
import matplotlib.pyplot as plt
from loadData import loadData
from sklearn import neighbors
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import plot_confusion_matrix

######################### LOAD DATA ##############################################
testF = 'dp210'
trainF = ['5pourcent/dataset145_a']
inj_Xtr, load_Xtr, gen_Xtr, secuN_Ytr, xte, secuN_Yte = loadData(testF, trainF)
xtr = [ inj_Xtr, load_Xtr, gen_Xtr]

######################### GLOBAL SETTINGS #######################################
#param_grid = {'n_neighbors': np.arange(1, 202, 10),
#              'metric': ['euclidean', 'manhattan','minkowski'],
#              'weights' : ['uniform','distance'],
#              'algorithm' : ['auto', 'ball_tree', 'kd_tree', 'brute'] }
param_grid0 = { 'n_neighbors': np.arange( 2, 21, 2) }
param_grid1 = { 'n_neighbors': np.arange( 2, 21, 2) }
param_grid2 = { 'n_neighbors': np.arange( 22, 41, 2) }
model = [ GridSearchCV( neighbors.KNeighborsClassifier(), param_grid0, cv=5),
          GridSearchCV( neighbors.KNeighborsClassifier(), param_grid1, cv=5),
          GridSearchCV( neighbors.KNeighborsClassifier(), param_grid2, cv=5)]
           
######################### MACHINE LEARNING #######################################
for Fe in [0,1,2]: # all kind of features
    print('fiting... ')
    model[Fe].fit( xtr[Fe], secuN_Ytr.ravel()) # grid search CV
    if Fe == 0: typeF = 'Injected'
    elif Fe == 1: typeF = 'Load'
    else: typeF = 'Gen'
    print( typeF, 'best : ', model[Fe].best_params_)   
plt.show()
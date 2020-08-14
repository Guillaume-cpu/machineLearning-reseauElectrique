import scipy.io
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import plot_confusion_matrix, confusion_matrix

######################### LOAD DATASET ###########################################
folder = 'dp210' # select dataset 
data = scipy.io.loadmat('dataset/' + folder + '/dataset.mat')
secuN_Y = np.array(data['secuN_Y'])
secuN1_Y = np.array(data['secuN1_Y'])
injected_X = np.array(data['injected_X'])   ################################### 
load_X = np.array(data['load_X'])           ## np.array [lignes] [col]
gen_X = np.array(data['load_X'])            ###################################

######################### GLOBAL SETTINGS ########################################
data_sampling = 96 # 96 value for one day (1/4 d'heure)
train_duration = 9 # Duration of the training set (15 day in total) 

######################### SELECT TRAINING & TESTING SET ##########################
begin = train_duration*data_sampling # Training start at the beginning of the set
# Training set
inj_X_train = injected_X[:begin]    
load_X_train = load_X[:begin]           
gen_X_train = gen_X[:begin]
secuN_Y_train = secuN_Y[:begin]
secuN1_Y_train = secuN1_Y[:begin]
# Testing set 
inj_X_test = injected_X[begin:]    
load_X_test = load_X[begin:]           
gen_X_test = gen_X[begin:]
secuN_Y_test = secuN_Y[begin:]
secuN1_Y_test = secuN1_Y[begin:]
# print( gen_X.shape, gen_X_train.shape, gen_X_test.shape)

######################### MACHINE LEARNING #######################################
print('________________KNN________________\n')

modelNames = [ 'injected', 'load', 'generation']
xtr = [ inj_X_train, load_X_train, gen_X_train]
xte = [ inj_X_test, load_X_test, gen_X_test]

# for k in range(1,41,2):
#     print( '-------', modelNames[1],  ' k =', k, '-------')
#     model = neighbors.KNeighborsClassifier(k)
#     model.fit( xtr[1], secuN_Y_train.ravel())
# #     print( 'train score :', round(models[i].score( xtr[i], secuN_Y_train),3))
#     print(confusion_matrix( model.predict(xtr[1]), secuN_Y_train))
# #     plot_confusion_matrix( models[i].best_estimator_, xte[i], secuN_Y_test)

model = MLPClassifier()
model.fit( xtr[1], secuN_Y_train.ravel())
print(confusion_matrix( model.predict(xte[1]), secuN_Y_test))



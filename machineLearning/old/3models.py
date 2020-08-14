import scipy.io
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC, LinearSVC
from sklearn import neighbors
from sklearn.metrics import confusion_matrix, plot_confusion_matrix

######################### LOAD DATASET ###########################################
folder = 'dp200' # select dataset 
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

modelNames = [ 'injected', 'load', 'generation']
models = [SVC( kernel='rbf', C=10, gamma=.00001) for i in range(3)]
xtr = [ inj_X_train, load_X_train, gen_X_train]
xte = [ inj_X_test, load_X_test, gen_X_test]

# print('________________SVC________________\n')
# for i in range(3):
#     print( '-------', modelNames[i], '-------')
#     models[i].fit( xtr[i], secuN_Y_train.ravel()) # Train the model
#     print( 'train score :', round(models[i].score( xtr[i], secuN_Y_train),3))
#     print( 'test score :', round(models[i].score( xte[i], secuN_Y_test),3), '\n')
#     # train values 
#     print(confusion_matrix( models[i].predict(xtr[i]), secuN_Y_train))
#     plot_confusion_matrix( models[i], xtr[i], secuN_Y_train)
#     # test values 
#     print(confusion_matrix( models[i].predict(xte[i]), secuN_Y_test))
#     plot_confusion_matrix( models[i], xte[i], secuN_Y_test)
    
models = [neighbors.KNeighborsClassifier(50, weights='uniform') for i in range(3)]
print('________________KNN________________\n')
for i in range(3):
    print( '-------', modelNames[i], '-------')
    models[i].fit( xtr[i], secuN_Y_train.ravel()) # Train the model
    print( 'train score :', round(models[i].score( xtr[i], secuN_Y_train),3))
    print( 'test score :', round(models[i].score( xte[i], secuN_Y_test),3), '\n')
    # train values 
    print(confusion_matrix( models[i].predict(xtr[i]), secuN_Y_train))
    plot_confusion_matrix( models[i], xtr[i], secuN_Y_train)
    
#     # test values 
#     print(confusion_matrix( models[i].predict(xte[i]), secuN_Y_test))
#     plot_confusion_matrix( models[i], xte[i], secuN_Y_test)
    
# models = [LinearSVC() for i in range(3)]
# print('_____________LinearSVC_____________\n')
# for i in range(3):
#     print( '-------', modelNames[i], '-------')
#     models[i].fit( xtr[i], secuN_Y_train.ravel()) # Train the model
#     print( 'train score :', round(models[i].score( xtr[i], secuN_Y_train),3))
#     print( 'test score :', round(models[i].score( xte[i], secuN_Y_test),3), '\n')
#     # train values 
#     print(confusion_matrix( models[i].predict(xtr[i]), secuN_Y_train))
#     plot_confusion_matrix( models[i], xtr[i], secuN_Y_train)
#     # test values 
#     print(confusion_matrix( models[i].predict(xte[i]), secuN_Y_test))
#     plot_confusion_matrix( models[i], xte[i], secuN_Y_test)
    
plt.show()

    # # Use the model on the testing features
    # moo = svr_model.predict(inj_X_test)     
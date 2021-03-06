import pickle
from classes import *
from loadData import loadData
from sklearn import neighbors
from sklearn.metrics import plot_confusion_matrix
import matplotlib.pyplot as plt

######################### LOAD DATA ##############################################
testF = 'dp210'
trainF = ['5pourcent/dataset145_a','5pourcent/dataset145_b',
          '5pourcent/dataset145_c', '5pourcent/dataset145_d']
# trainF = ['5pourcent/dataset145_a']
inj_Xtr, load_Xtr, gen_Xtr, secuN_Ytr, xte, secuN_Yte = loadData(testF)

######################### GLOBAL SETTINGS ########################################
data_sampling = 96 # 96 value for one day (1/4 d'heure)
model = Models([ neighbors.KNeighborsClassifier(4),
                 neighbors.KNeighborsClassifier(4),
                 neighbors.KNeighborsClassifier(22) ])
class_names = ['Saine','Risquée']

######################### SELECT TRAININGSET #####################################
# for trainDay in [1,2,3,4,5,6,7,14,28,60,90,145,180,360,720,1080,1440]:
for trainDay in [720]:
    begin = trainDay*data_sampling 
    inj_X_train = inj_Xtr[-begin:] # Training start at the en of the trainset   
    load_X_train = load_Xtr[-begin:]            
    gen_X_train = gen_Xtr[-begin:] 
    secuN_Y_train = secuN_Ytr[-begin:] 
#     secuN1_Y_train = secuN1_Ytr[:begin]
    xtr = [ inj_X_train, load_X_train, gen_X_train]
    print(trainDay)
    #################### MACHINE LEARNING ########################################
#     for Fe in range(3): # all kind of features
    for Fe in [2]:        
        model.estimateur[Fe].fit( xtr[Fe], secuN_Y_train.ravel()) # Train the model
#         confM = confusion_matrix( secuN_Yte, model.estimateur[Fe].predict(xte[Fe]))
        plot_confusion_matrix( model.estimateur[Fe], xte[Fe], secuN_Yte, display_labels=class_names,)
#         if Fe == 0:
#             saveConfM(model.confM.inj,trainDay,confM)
#         elif Fe == 1:
#             saveConfM(model.confM.load,trainDay,confM)
#         elif Fe == 2:
#             saveConfM(model.confM.gen,trainDay,confM)
plt.show()
# pickle.dump(model.confM,open('confusionData/5pourcent/'+ testF+ '/knn.pickle','wb'))
import scipy.io
import numpy as np
import pickle
from sklearn.svm import SVC
from sklearn import neighbors
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix

class Functions():
    def __init__(self):
        self.x = []
        self.f1 = []
        self.f2 = []
        self.f3 = []
        self.f4 = []

class TypeFeatures():
    def __init__(self):
        self.inj = Functions()
        self.load = Functions()
        self.gen = Functions()

class Models():
    def __init__(self, estimateur):
        self.estimateur = estimateur
        self.confM = TypeFeatures()

######################### TRAINSET ##############################################
trainFile = 'dataset12_a' 
trainData = scipy.io.loadmat('dataset/train/'+ trainFile)
secuN_Ytr = np.array(trainData['secuN_Y'])
# secuN1_Ytr = np.array(data['secuN1_Y'])
injected_Xtr = np.array(trainData['injected_X'])    
load_Xtr = np.array(trainData['load_X'])           
gen_Xtr = np.array(trainData['gen_X'])             

######################### TESTSET ###############################################
testFile = 'dp200'
testData = scipy.io.loadmat('dataset/test'+ testFile+ '/dataset.mat')
secuN_Yte = np.array(testData['secuN_Y'])
# secuN1_Yte  = np.array(data['secuN1_Y'])
injected_Xte= np.array(testData['injected_X']) 
load_Xte = np.array(testData['load_X'])          
gen_Xte = np.array(testData['gen_X'])
Xte = [ injected_Xte, load_Xte, gen_Xte]

######################### GLOBAL SETTINGS #######################################
data_sampling = 96 # 96 value for one day (1/4 d'heure)
model = Models( SVC( kernel='rbf', C=10, gamma=.00001))
# models = [ Models( SVC( kernel='rbf', C=10, gamma=.00001)),
#            Models( neighbors.KNeighborsClassifier(50, weights='uniform')),
#            Models( RandomForestClassifier()),
#            Models( MLPClassifier()) ]

######################### SELECT TRAININGSET ####################################
for trainDay in range( 1, len( secuN_Ytr) / data_sampling, 7):
    
    begin = trainDay*data_sampling 
    inj_X_train = injected_Xtr[-begin:] # Training start at the en of the trainset   
    load_X_train = load_Xtr[-begin:]            
    gen_X_train = gen_Xtr[-begin:] 
    secuN_Y_train = secuN_Ytr[-begin:] 
#     secuN1_Y_train = secuN1_Ytr[:begin]
    xtr = [ inj_X_train, load_X_train, gen_X_train]

    #################### MACHINE LEARNING #######################################
    for Fe in range(3): # all kind of features
        model.estimateur.fit( xtr[Fe], secuN_Y_train.ravel()) # Train the model
        confM = confusion_matrix( secuN_Yte, model.predict(xte[Fe]))
        if Fe == 0:
            model.confM.inj.x.append(trainDay)
            model.confM.inj.f1.append(confM[0][0])
            model.confM.inj.f2.append(confM[0][1])
            model.confM.inj.f3.append(confM[1][0])
            model.confM.inj.f4.append(confM[1][1])
        elif Fe == 1:
            model.confM.inj.x.append(trainDay)
            model.confM.load.f1.append(confM[0][0])
            model.confM.load.f2.append(confM[0][1])
            model.confM.load.f3.append(confM[1][0])
            model.confM.load.f4.append(confM[1][1])
        elif Fe == 1:
            model.confM.inj.x.append(trainDay)
            model.confM.gen.f1.append(confM[0][0])
            model.confM.gen.f2.append(confM[0][1])
            model.confM.gen.f3.append(confM[1][0])
            model.confM.gen.f4.append(confM[1][1])
            
pickle.dump(model,'models/svc')

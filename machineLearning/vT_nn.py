import pickle
from classes import *
from loadData import loadData
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix

######################### LOAD DATA #############################################
testF = 'dp210'
trainF = ['5pourcent/dataset145_a','5pourcent/dataset145_b',
          '5pourcent/dataset145_c', '5pourcent/dataset145_d']
# inj_Xtr, load_Xtr, gen_Xtr, secuN_Ytr, xte, secuN_Yte = loadData(testF, trainF)
inj_Xtr, load_Xtr, gen_Xtr, secuN_Ytr, xte, secuN_Yte = loadData(testF, trainF)

######################### GLOBAL SETTINGS #######################################
data_sampling = 96 # 96 value for one day (1/4 d'heure)
model = Models([ MLPClassifier( hidden_layer_sizes=(120,120,120,120,120) , max_iter = 100),
                 MLPClassifier( hidden_layer_sizes=(120,120,120,120,120) , max_iter = 100),
                 MLPClassifier(hidden_layer_sizes=(70,) , max_iter = 100) ])

######################### SELECT TRAININGSET ####################################
#for trainDay in range( 1, round(len( secuN_Ytr) / data_sampling), 7):
# for trainDay in [1,2,3,4,5,6,7,14,28,60,90,145,180,360,720,1080,1440]:
for trainDay in [360]:
    begin = trainDay*data_sampling 
    inj_X_train = inj_Xtr[-begin:] # Training start at the en of the trainset   
    load_X_train = load_Xtr[-begin:]            
    gen_X_train = gen_Xtr[-begin:] 
    secuN_Y_train = secuN_Ytr[-begin:] 
#     secuN1_Y_train = secuN1_Ytr[:begin]
    xtr = [ inj_X_train, load_X_train, gen_X_train]
    #################### MACHINE LEARNING #######################################
    for Fe in range(2,3): # all kind of features
        model.estimateur[Fe].fit( xtr[Fe], secuN_Y_train.ravel()) # Train the model
        print(model.estimateur[Fe].n_layers_)
        confM = confusion_matrix( secuN_Yte, model.estimateur[Fe].predict(xte[Fe]))
        if Fe == 0:
            saveConfM(model.confM.inj,trainDay,confM)
        elif Fe == 1:
            saveConfM(model.confM.load,trainDay,confM)
        elif Fe == 2:
            saveConfM(model.confM.gen,trainDay,confM)
        
print('\n Injection')
print( 'fausse alarme', model.confM.inj.f2)
print( 'non-détection', model.confM.inj.f3)
print('\n Load')
print( 'fausse alarme', model.confM.load.f2)
print( 'non-détection', model.confM.load.f3)
print('\n Gen')
print( 'fausse alarme', model.confM.gen.f2)
print( 'non-détection', model.confM.gen.f3)
# pickle.dump(model.confM,open('confusionData/5pourcent/'+ testF+ '/nn.pickle','wb'))
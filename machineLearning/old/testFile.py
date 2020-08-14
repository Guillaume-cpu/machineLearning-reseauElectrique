import numpy as np
# trainFiles = [ 'dataset12_a', 'dataset12_b', 'dataset12_c', 'dataset13_d']
# 
# for trainFile in trainFiles[1:]:
#     print(trainFile)

# a = np.array([])
# b = np.array([[1, 2], [3, 4]])
# print(b)
# c = np.array([[5, 6],[7,8]])
# print(c)
# a = np.concatenate((b, c), axis=0)

# a = [i for i in range(1,7)] + [i for i in range(28,180,30)]
# for i in a:
#     print(i)
# print(a)
# c = np.array([1.3,2.2,3.3,4.3])
# a = np.concatenate((a,c),1)
# print(a)

# import scipy.io
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.svm import SVC, LinearSVC
# from sklearn import neighbors
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.neural_network import MLPClassifier
# from sklearn.metrics import confusion_matrix, plot_confusion_matrix
# 
# 
#         
# ######################### TRAINSET ##############################################
# trainFolder = 'year1' 
# trainData = scipy.io.loadmat('bigDataset/dataset/' +
#                              trainFolder + '/dataset.mat')
# secuN_Ytr = np.array(trainData['secuN_Y'])
# # secuN1_Ytr = np.array(data['secuN1_Y'])
# injected_Xtr = np.array(trainData['injected_X'])    
# load_Xtr = np.array(trainData['load_X'])           
# gen_Xtr = np.array(trainData['gen_X'])             
# 
# ######################### GLOBAL SETTINGS #######################################
# data_sampling = 96 # 96 value for one day (1/4 d'heure)
# models = [ neighbors.KNeighborsClassifier(50, weights='uniform')]
# functions = [ Func(), Func(), Func()]
# # models = [ SVC( kernel='rbf', C=10, gamma=.00001),
# #            neighbors.KNeighborsClassifier(50, weights='uniform'),
# #            RandomForestClassifier(),
# #            MLPClassifier ]
# 
# ######################### SELECT TRAININGSET ####################################
# # for trainDay in range( 1, len( secuN_Ytr) / data_sampling, 7):
# for trainDay in [1,7,30,100,300]:
#     begin = trainDay*data_sampling 
#     inj_X_train = injected_Xtr[-begin:] # Start at the en of the trainset   
#     load_X_train = load_Xtr[-begin:]            
#     gen_X_train = gen_Xtr[-begin:] 
#     secuN_Y_train = secuN_Ytr[-begin:] 
# #     secuN1_Y_train = secuN1_Ytr[:begin]
#     xtr = [ inj_X_train, load_X_train, gen_X_train]
# 
#     #################### MACHINE LEARNING #######################################
#     for model in models: # all models
#         for Fe in range(3): # all kind of features
#             model.fit( xtr[Fe], secuN_Y_train.ravel()) # Train the model
#             confM = confusion_matrix( secuN_Y_train, model.predict(xtr[Fe]))
#             print(confM)
#             plot_confusion_matrix( model, xtr[Fe], secuN_Y_train)
#             
#             functions[Fe].f1.append(confM[0][0])
#             functions[Fe].f2.append(confM[0][1])
#             functions[Fe].f3.append(confM[1][0])
#             functions[Fe].f4.append(confM[1][1])
# 
# for typeF in functions:
#     print('\n----------------')
#     for funct in [ typeF.f1, typeF.f2, typeF.f3, typeF.f4]:
#         print('\n *****************')
#         for i in funct:
#             print(i)
#         
# plt.show()    
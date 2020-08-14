import pickle
import matplotlib.pyplot as plt
from classes import *
import numpy as np
import scipy.io

testFile = 'dp210'
modelNames = ['kNN','SVC','NN','RF']
models = []
for i in range(4):    
    file = 'confusionData/5pourcent/'+ testFile+ '/'+ modelNames[i]+ '.pickle'
#     file = 'confusionData/'+ testFile+ '/'+ modelNames[i]+ '.pickle'
    models.append(pickle.load(open(file,'rb')))
injection = []
charge = []
production =[] 
injection.append(models[i].inj.x)
charge.append(models[i].load.x)
production.append(models[i].gen.x)
for i in range(4):    
    injection.append(models[i].inj.f2)
    injection.append(models[i].inj.f3)
    charge.append(models[i].load.f2)
    charge.append(models[i].load.f3)
    
    if len(models[i].gen.f2) == 16:
        production.append(np.append([0],models[i].gen.f2))
    else: 
        production.append(models[i].gen.f2)
        
    if len(models[i].gen.f3) == 16:
        production.append(np.append([0],models[i].gen.f3))
    else: 
        production.append(models[i].gen.f3)

   
scipy.io.savemat('normal.mat', mdict={'injection': injection,'charge':charge,'production':production })
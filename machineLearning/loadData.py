import scipy.io
import numpy as np
from classes import *

def loadData(testFile, trainFiles = [ 'dataset12_a', 'dataset12_b', 'dataset12_c', 'dataset13_d']):
    ######################### TRAINSET ##############################################
    injected_Xtr, load_Xtr, gen_Xtr, secuN_Ytr = extract(trainFiles[0])
    print( trainFiles[0], sum(secuN_Ytr==1), sum(secuN_Ytr==0))
    for trainFile in trainFiles[1:]:
        injected, load, gen, secuN = extract(trainFile)
        print( trainFile, sum(secuN==1), sum(secuN==0))
        injected_Xtr = conc(injected_Xtr,injected)
        load_Xtr = conc(load_Xtr,load)
        gen_Xtr = conc(gen_Xtr,gen)
        secuN_Ytr = conc(secuN_Ytr,secuN)
    print( 'All train files', sum(secuN_Ytr==1), sum(secuN_Ytr==0))

    ######################### TESTSET ###############################################
    testData = scipy.io.loadmat('dataset/test/'+ testFile+ '/dataset.mat')
    secuN_Yte = np.array(testData['secuN_Y'])
    # secuN1_Yte  = np.array(data['secuN1_Y'])
    injected_Xte= np.array(testData['injected_X']) 
    load_Xte = np.array(testData['load_X'])          
    gen_Xte = np.array(testData['gen_X'])
    xte = [ injected_Xte, load_Xte, gen_Xte]
    print( 'Test file', sum(secuN_Yte==1), sum(secuN_Yte==0))
    
    return injected_Xtr, load_Xtr, gen_Xtr, secuN_Ytr, xte, secuN_Yte
if __name__ == '__main__':
    trainF = ['5pourcent/dataset145_a','5pourcent/dataset145_b',
          '5pourcent/dataset145_c', '5pourcent/dataset145_d']
    loadData('dp200', trainF)
         
    
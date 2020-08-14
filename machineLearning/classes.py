import scipy.io
import numpy as np

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
    def __init__(self, estimateurs):
        self.estimateur = estimateurs
        self.confM = TypeFeatures()
        
def extract(trainFile):
    trainData = scipy.io.loadmat('dataset/train/'+ trainFile)
    secuN_Ytr = np.array(trainData['secuN_Y'])
    # secuN1_Ytr = np.array(data['secuN1_Y'])
    injected_Xtr = np.array(trainData['injected_X'])
    injected_Xtr = np.delete(injected_Xtr,0,1)
    injected_Xtr = np.delete(injected_Xtr,56,1)
    load_Xtr = np.array(trainData['load_X'])
    load_Xtr = np.delete(load_Xtr,0,1)
    gen_Xtr = np.array(trainData['gen_X'])
    gen_Xtr = np.delete(gen_Xtr,0,1)
    return injected_Xtr, load_Xtr, gen_Xtr, secuN_Ytr

def conc(old,new):
    old = np.concatenate((old,new),0)
    return old

def saveConfM(model,trainDay,confM):
    model.x.append(trainDay)
    model.f1.append(confM[0][0])
    model.f2.append(confM[0][1])
    model.f3.append(confM[1][0])
    model.f4.append(confM[1][1])
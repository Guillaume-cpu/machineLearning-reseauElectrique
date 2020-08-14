import numpy
from loadData import loadData
testF = 'dp210'
# trainF = ['5pourcent/dataset145_a','5pourcent/dataset145_b',
#           '5pourcent/dataset145_c', '5pourcent/dataset145_d']
trainF = ['5pourcent/dataset145_a']
inj_Xtr, load_Xtr, gen_Xtr, secuN_Ytr, xte, secuN_Yte = loadData(testF, trainF)
print(secuN_Ytr.shape,secuN_Ytr.ravel().shape)
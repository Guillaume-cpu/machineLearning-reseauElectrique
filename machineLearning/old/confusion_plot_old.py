import pickle
import matplotlib.pyplot as plt
from classes import *

def plot_same( typeF, name, feature, i):
    plt.subplot(4,3,i)
    plt.title(name+ ' - '+ feature, fontsize=20)
    plt.scatter( typeF.x, typeF.f2, label = 'Fausse alarme')
    
#     for i_x, i_y in zip(typeF.x, typeF.f2):
#         plt.text(i_x, i_y, '  {}'.format( i_y), fontsize =  'x-large')
        
    plt.scatter( typeF.x, typeF.f3, label = 'Non-détection')
    
#     for i_x, i_y in zip(typeF.x, typeF.f3):
#         plt.text(i_x, i_y, '  {}'.format( i_y), fontsize =  'x-large')
        
    plt.ylim(( 0, 350))        
    plt.xlabel('# jours d\'entrainement')
    plt.ylabel('# cas')
    plt.legend()
    return i+1

def plot_cf( model, name, i):
    i = plot_same( model.inj, name, 'injections', i)
    i = plot_same( model.load, name, 'charges', i)
    i = plot_same( model.gen, name, 'productions', i)
    return i
    
######################### PLOT CM ##############################################
# modelNames = ['knn','rf']
testFile = 'dp200'
testName = 'alourdi'
modelNames = ['knn','svc','nn','rf']
i = 1
for name in modelNames:
    
#     file = 'confusionData/5pourcent/'+ testFile+ '/'+ name+ '.pickle'
    file = 'confusionData/'+ testFile+ '/'+ name+ '.pickle'
    
    model = pickle.load(open(file,'rb'))
    i = plot_cf( model, name, i)
plt.suptitle('Scénrio '+ testName, fontsize=22)
plt.subplots_adjust(left=0.05, bottom=0.06, right=0.97,
                    top=0.92, wspace=0.17, hspace=0.34)
fig = plt.gcf()
fig.set_size_inches(18.5, 10.5)
plt.show()
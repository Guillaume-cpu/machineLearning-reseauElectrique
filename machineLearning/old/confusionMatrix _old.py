import pickle
import matplotlib.pyplot as plt
from classes import *
        
def plotting( typeF, name, feature):
    plt.figure()
    plt.suptitle('Modèle '+ name+ ' avec les '+ feature, fontsize=20)
    for i in range(1,5):
        plt.subplot(2,2,i)
        if i == 1:
            plt.scatter(typeF.x,typeF.f1)
            m = max(typeF.f1)
        elif i == 2:
            plt.scatter(typeF.x,typeF.f2)
            m = max(typeF.f2)
        elif i == 3:
            plt.scatter(typeF.x,typeF.f3)
            m = max(typeF.f3)
        elif i == 4:
            plt.scatter(typeF.x,typeF.f4)
            m = max(typeF.f4)
        
        plt.ylim(( 0, 1.1*m))    
        plt.title('f'+ str(i))    
        plt.xlabel('# train day')

def plot4(model, name):
    plotting( model.inj, name, 'injections')
    plotting( model.load, name, 'charges')
    plotting( model.gen, name, 'production')

def plot_same( typeF, name, feature, i):
    plt.subplot(4,3,i)
    plt.title('Modèle '+ name+ ' avec les '+ feature, fontsize=20)
#     plt.scatter( typeF.x, typeF.f1, label = 'f1')
    plt.scatter( typeF.x, typeF.f2, label = 'f2')             
    plt.scatter( typeF.x, typeF.f3, label = 'f3')
#     plt.scatter( typeF.x, typeF.f4, label = 'f4')
#     m = max(max([typeF.f1,typeF.f2,typeF.f3,typeF.f4]))
    m = max(max([typeF.f2,typeF.f3]))
    plt.ylim(( 0, 380))        
    plt.xlabel('# jour d''entrainement')
    plt.ylabel('# des cas')
    plt.legend()
    return i+1

def plot1( model, name, i):
    i = plot_same( model.inj, name, 'injections', i)
    i = plot_same( model.load, name, 'charges', i)
    i = plot_same( model.gen, name, 'production', i)
    return i

def compare( models, name, features, j):
    plt.subplot(1,3,j)
    plt.title('Modèles avec les '+ features, fontsize=16)
    plt.scatter( models.x, models.f2, label = 'f2 ' + name)             
    plt.scatter( models.x, models.f3, label = 'f3 ' + name, marker = 'X')        
    plt.xlabel('# jour d''entrainement')
    plt.ylabel('# des cas')
    plt.legend()

def comparaison(models,name):
    compare(models.inj, name, 'injections', 1)
    compare(models.load, name, 'charges', 2)
    compare(models.gen, name, 'productions', 3)
    
######################### PLOT CM ##############################################
# modelNames = ['knn','rf']
modelNames = ['knn','svc','nn','rf']
i = 1
for name in modelNames:
    file = 'models/' + name + '.pickle'
    model = pickle.load(open(file,'rb'))
#     plot4( model, name)
    i = plot1( model, name, i)
#     comparaison( model, name) # Trop d'information 
plt.show()
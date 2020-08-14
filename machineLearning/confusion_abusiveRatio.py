import pickle
import numpy as np 
def see( name, model):
    print('-----', name, '-----\n')
    print('injection - alarme abusive', model.inj.f2, '\n')
    print('injection - risque non détectée', model.inj.f3, '\n')
    print('load - alarme abusive', model.load.f2, '\n')
    print('load - risque non détectée', model.load.f3, '\n')
    print('gen - alarme abusive', model.gen.f2, '\n')
    print('gen - risque non détectée', model.gen.f3, '\n')

def ratioAbusive( name, m):
    print('--------', name, '- Ratio alarme abusive --------\n')
    ratio = np.divide( m.f2, np.add(m.f4,np.add(m.f3,m.f2)))
    print('Injection ', ratio, '\n')

######################### Plot specifique value ########################
# modelNames = ['knn','svc','nn','rf']
testFile = 'dp215'
modelNames = ['svc']
for name in modelNames:
    file = 'confusionData/'+ testFile+ '/'+ name+ '.pickle'
    model = pickle.load(open(file,'rb'))
#     see( name, model)
    ratioAbusive( name, model.gen)

## trainDay = [1,2,3,4,5,6,7,14,28,60,90,145,180,360,720,1080,1440] ####
  

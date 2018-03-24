def modification(data):
    for train in data:
        countCar=0
        for car in train['cars']:
            countCar+=1
            countPepl=0
            for man in car['people']:
                countPepl+=1
            car['count']=countPepl
            car['num']=countCar-1
        train['count']=countCar
    return data

def poiskvagona(data, numb):
    for train in data:
        for car in train['cars']:
                if numb == car['name']:
                    return car
    return -1

def poiskpoizda (inf, name):
    for train in inf:
        for car in train['cars']:
            for man in car['people']:
                if name==man:
                    return train
    return -1

def poiskname(train,name):
    for car in train['cars']:
        for man in car['people']:
            if name == man:
                return car['name']
    return 1

def poisknumpep(car,str):
    c=0
    for name in car['people']:
        if name==str:
            return c
        c+=1

def poiskponum(poizd,num):
    for car in poizd['cars']:
        if car['num']==num:
            return car
    return -1
def poiskpoizdapoimeni(data,name):
    for train in data:
         if train['name']== name:
                return train

def obrabotka(data, event):
   if event.get('type') == 'walk':
     try:
      poizd=poiskpoizda(data,event['passenger'])
     except Exception:
         return -1
     name=poiskname(poizd,event['passenger'])
     vagon=poiskvagona(data,name)
     sum=vagon['num']+event['distance']
     if (sum>-1 and sum<poizd['count']):
         k=poisknumpep(vagon,event['passenger'])
         vagon['people'].pop(k)
         vagon['count']-=1
         vagon=poiskponum(poizd,sum)
         vagon['people'].append(event['passenger'])
         vagon['count']+=1
     else:
         return -1
     return data
   else:
     poizdprom={}
     poizd = poiskpoizdapoimeni(data, event['train_from'])
     poizdto = poiskpoizdapoimeni(data, event['train_to'])
     vagon = poiskponum(poizd, poizd['count'] - 1)
     vagon['num']=0
     poizdprom['cars'] = [vagon]
     n=event['cars']
     poizd['cars'].pop()
     poizd['count'] -= 1
     poizdprom['count']=n
     for i in range(1,n,1):
       vagon=poiskponum(poizd,poizd['count']-1)
       vagon['num'] = i
       poizdprom['cars'].append(vagon)
       poizd['cars'].pop()
       poizd['count'] -= 1
     for k in range(0,n,1):
       vagon=poiskponum(poizdprom,poizdprom['count']-1)
       vagon['num']=poizdto['count']
       poizdto['cars'].append(vagon)
       poizdto['count']+=1
       poizdprom['cars'].pop()
       poizdprom['count'] -= 1
     return data

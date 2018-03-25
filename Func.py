def poiskvagona(data, numb):
    for train in data:
        for car in train['cars']:
                if numb == car['name']:
                    return car
    return -1
def poisknumcar(poizd,str):
    c = 0
    for car in poizd['cars']:
        if car['name'] == str:
            return c
        c += 1

def poisknumpep(car,str):
    c=0
    for name in car['people']:
        if name==str:
            return c
        c+=1

def poiskponum(poizd,num):
    c=0
    for car in poizd['cars']:
        if poisknumcar(poizd,car['name'])==num:
            return car
        c+=1
    return -1

def poiskpoizdapoimeni(data,name):
    for train in data:
         if train['name']== name:
                return train

def poisk(inf, name):
    for train in inf:
        for car in train['cars']:
            for man in car['people']:
                if name==man:
                    return train,car
    return -1

def obrabotka(data, event):
   if event.get('type') == 'walk':
     poizd,vagon=poisk(data,event['passenger'])
     sum=poisknumcar(poizd,vagon['name'])+event['distance']
     if (sum>-1 and sum<len(poizd['cars'])):
         k=poisknumpep(vagon,event['passenger'])
         vagon['people'].pop(k)
         vagon=poiskponum(poizd,sum)
         vagon['people'].append(event['passenger'])
     else:
         return -1
     return data
   else:
     poizd = poiskpoizdapoimeni(data, event['train_from'])
     poizdto = poiskpoizdapoimeni(data, event['train_to'])
     n=event['cars']
     if n<1:
         return -1
     poizdprom = poizd['cars'][-n:]
     for i in range(1,len(poizdprom)+1,1):
         poizd['cars'].pop()
     poizdto['cars'].extend(poizdprom)
     return data

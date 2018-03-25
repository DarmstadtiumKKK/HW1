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

     '''     vagon = poiskponum(poizd, poizd['count'] - 1)
     vagon['num']=0
     poizdprom['cars'] = [vagon]
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
       poizdprom['count'] -= 1'''
     return data

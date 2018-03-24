# -*- encoding: utf-8 -*-
from Func import obrabotka
from Func import poiskvagona
from Func import modification

def process(data, events, car):
    modification(data)
    for event in events:
     try:
      a=obrabotka(data, event)
      if a == -1:
          return -1
     except Exception:
        return -1
    try:
     vagon = poiskvagona(data,car)
    except TypeError:
        return -1
    return vagon['count']

    for train in data:
        print(train['name'])
        for car in train['cars']:
            print('\t{}'.format(car['name']))
            for man in car['people']:
                print('\t\t{}'.format(man))

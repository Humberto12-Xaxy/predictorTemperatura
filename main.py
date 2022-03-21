import pandas as pd
import numpy as np

def readDataSet():

    data = pd.read_csv('./dataset.csv')

    temp = data['temperatura']
    aux = []
    
    cont = 0
    prom = 0
    for i in range(len(temp)):

        cont += 1
        prom += temp[i]

        if cont == 24:
            cont = 0
            prom = prom / 24
            aux.append(prom)
            prom = 0       

    csv_temperatura = pd.DataFrame(aux, columns=['Temperatura'])
    csv_temperatura.to_csv('temperatura.csv', index= False)        


def readDataTemperatura():
    readDataSet()
    temperatura = pd.read_csv('./temperatura.csv')
    

readDataTemperatura()
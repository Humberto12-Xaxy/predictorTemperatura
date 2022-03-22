from pickletools import optimize
import pandas as pd
import numpy as np
import tensorflow as tf

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
    
    temperatura = pd.read_csv('./temperatura.csv')

    dataSetBueno = []

    for i in range(len(temperatura)-1):
        dataSetBueno.append([temperatura['Temperatura'][i], temperatura['Temperatura'][i+1]])
        
    csv_temperatura = pd.DataFrame(dataSetBueno, columns=['X','Y'])
    csv_temperatura.to_csv('EntradasYSalidas.csv', index= False)

def readDataEntradaYSalida():

    data = pd.read_csv('./EntradasYSalidas.csv')

    numDataToTrain = round(len(data['X']) * 0.8)

    X_toTrain = []
    Y_toTrain = []

    X_toTest = []
    Y_toTest = []

    for i in range(10):

        if i <= numDataToTrain:
            X_toTrain.append(data['X'][i])
            Y_toTrain.append(data['Y'][i])
        else:
            X_toTest.append(data['X'][i])
            Y_toTest.append(data['Y'][i])  

    print(X_toTrain)
    print(Y_toTrain)
    
    # COMENZAMOS ENTRAMIENTO

    capa1 = tf.keras.layers.Dense(units= 50, input_shape= [1], activation = 'linear')
    capa2 = tf.keras.layers.Dense(units= 50, activation = 'linear')
    capa3 = tf.keras.layers.Dense(units= 50, activation = 'linear')
    capa4 = tf.keras.layers.Dense(units= 50, activation = 'linear')
    salida = tf.keras.layers.Dense(units = 1)

    modelo = tf.keras.Sequential([capa1,capa2,capa3, capa4, salida])

    modelo.compile(
        optimizer = tf.keras.optimizers.Adam(0.000001),
        loss = 'mean_squared_error'
    )

    print('Entrenamiento')

    historial = modelo.fit(X_toTrain, Y_toTrain, epochs=5000, batch_size=64)

    print('Modelo entrenado')

    resultado = modelo.predict([3.4959452541666667])
    print(f'Resultado {resultado}')
    # 1.581361965833333

    # 1.9771952679166669

readDataEntradaYSalida()
import numpy as np
array = np.arange(0,16)
print(array)
print("--"*40)
print(array+array) #Soma indice por indice, funciona com outros operadores logicos
print(array + 100)#Soma um numero especifico, funciona com outros operadores e numeros
print(np.mean(array))#Retorna a media da array

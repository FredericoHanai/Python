import numpy as np
#sequencia de numeros, primeria casa antes da virgula, onde começa
#segunda casa depois da virgula, onde termina
#ultima casa, só se for necessario, "step"
print(np.arange(0,100,3))
print("---"*40)

#cria uma matriz de zeros, passa o parametro, se quiser uma matriz colocar ()
print(np.zeros((5,5)))
print("---"*40)

#matriz identidade, contem 1 na sua diagonal principal
print(np.eye(3))
print("---"*40)

#esse metodo mostra a quantidade passada por parametro, espaçada igualmente, só rodando pra ver
print(np.linspace(0,10,3))
print("---"*40)

array = np.random.rand(5)
print(array)
print("---"*40)
##escontarando o maior valor da array
print(array.max())
print("---"*40)
#encontrando o menor valor da array
print(array.min())
print("---"*40)

#retorna o indice onde o maior elemento se encontra
print(array.argmax())
print("---"*40)
#retorna o indice onde o menor elemento se encontra
print(array.argmin())

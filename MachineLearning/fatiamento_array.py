import numpy as np
array = np.arange(0,30,3)
print(array)
print("--"*40)
#definindo de 0 a 49 o tamanho do vetor
array = np.arange(50)
print(array)
print("--"*40)
#usando reshape vemos que ele fica com LINHAS  e dps COLUNAS, exemplo abaixo: (5 linhas e 10 colunas)
array = np.arange(50).reshape(5,10)
print(array)
print("--"*40)
#podemos ver a dimensao dessa matriz, utilizando o shape, exemplo abaixo
print(array.shape) #vai printar a quantidade de linha e de colunas.
print("--"*40)
#printando as linhas e colunas, o primeiro [] mostra a linha o segundo [] a coluna
print(array[:3])
print("--"*40)
#aqui a variavel array 2 recebe todos os elementos do vetor array até a linha 3, porem não é uma COPIA a variavel array2
#esta apontando para o array principal (variavel array)
array2 = array[:3]
print(array2)
print("--"*40)
#fazendo a copia da variavel array
array3 = array[:3].copy()
array3[:] = 10
print(array3)
print("--"*40)
#buscando valores dentro da array utilizando apenas um []
print(array)
print("--"*40)
print(array[0:3,:6])#utilizando a virgula, antes dela para procurar as linhas, dps dela para procurar as colunas
print("--"*40)
#extraindo alguns dados de dentro da array
#cria uma variavel qualquer recebendo o parametro, nesse caso abaixo, vai mostrar os indices maiores que 24
bol = array > 24
print(array[bol])#coloca primeiro a variavel de lista e dps a variavel que foi passada como parametro
print("--"*40)
#array = np.arange(30).reshape(5,6)
#print (array)
#print("--"*40)
#print(array[1:2,1:2])
#DICA: passa o numero da linha, (lembrando que começa em 0) e dps uma a mais, por parametro onde termina não conta
#faça mesma coisa para pegar a coluna
#Exemplo, quer linha 1 coluna 2 |ex:  [1:2,2:3]
#dentro do metodo SUM do numpy existe o parametro 'axis', usado para somar linhas e colunas, parametro ou seja,
#axis = 0 soma as colunas e axis = 1 soma as linhas.
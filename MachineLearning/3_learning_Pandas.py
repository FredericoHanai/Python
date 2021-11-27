import numpy as np
import pandas as pd
#DataFrame são conjunto de series.
labels = ['a','b','c']
minha_lista = [10,20,30]
arra = ([10,20,30])
d = {'a':10,'b':20,'c':30}

series = pd.Series(data=minha_lista,index=labels) #associar como se fosse um dicionario, nesse caso os valors 10,20,30 esta associadoa com a variavel labels que recebe a,b,c
#print(series)

serie1 = pd.Series([1,2,3,4],index=['EUA', 'Alemanha', 'URSS','Japão'])
serie2 = pd.Series([1,2,3,4],index=['EUA', 'Alemanha', 'Italia','Japão'])

#print(serie1+serie2) #Neste momento tentando "Somar" as variaveis devolve o indice somado e o que tem nesse indice.

np.random.seed(101)
df = pd.DataFrame(np.random.randn(5,4),index = 'A B C D E'.split(), columns = 'W X Y Z'.split())
print(df)
print('--'*40)
print(df['W']) #printando a coluna W, poderia printar qualquer outra coluna que definimos acima "W X Y Z", colocando como parametro
print('--'*40)
print(df[['X', 'W']]) # para puxas multiplas colunas precisa abrir outra 'lista' ou seja, [[]] e passar o parametro
print('--'*40)
df['new'] = df['W'] + df['X'] #criando uma nova coluna no DataFrame
print(df) #comprovando
print('--'*40)
df.drop('new',axis=1,inplace=True) #excluindo a coluna new
print(df) #comprovando
print('--'*40)
#localizar indices dentro desse "Excel"
print(df.loc['A','W']) #passa primeiro a linha como parametro e apos a coluna, muito semelhante ao numpy arrays
print(df.loc[['A','B'], ['X','Y', 'Z']]) #pegando varios indices, NAO ESQUECER DOS []
print('--'*40)
print(df)
print(df.iloc[1:4,2:]) # encontrando os elementos no mesmo metodo do numpy
print('--'*40)
bol = df > 0
print(df[bol]) #printando valores que sao maiores que 0, lembrando de definir uma variavel pra isso, senao retorna um valor boolean
print('--'*40)
print(df[df['W']>0])
print(df[df['W']>0]['Y']) #fazendo slices para retornar valores maiores que 0 dentro da coluna Y aos quais os valores da W sao maios que 0
print('--'*40)
print(df[(df['W'] > 0) & (df['Y']>1) ]) #usando o E comercial vulgo &, podemos fazer a comparação de SERIES, o and não se comporta muito bem nesse caso
print('--'*40)
df.reset_index() #reseta o index, se quiser que isso aconteça coloque como paramentro o inplace = True
df.set_index() #definindo alguma coluna como index, para fazer isso, coloque a varivael como parametro
print('--'*40)


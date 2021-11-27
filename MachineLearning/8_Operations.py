import pandas as pd
df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})
print(df.head())
print('--'*40)
#Primeiro metodo, metodo de selecao de dados unicos, vai apontar a coluna que contem valor unico (especifico)
print(df['col2'].unique())
print(df['col2'].nunique())#retorna o tamanho do vetor que colocou no paramentro, parecido com o metodo length
print(df['col2'].value_counts())#retorna os valores unicos e a quatidade de vzs que ele aparece
print('--'*40)
#df['col1'].apply() permite usar uma função criada por vc, colocar no parametro a funçaõ

#saber o tamanho da string na coluna 3
print(df.head())
print('--'*40)
print(df['col3'].apply(len))
print('--'*40)
#deletar colunas
del df['col2']
print('--'*40)
print(df.columns) #Quais os valores da coluna
print(df.index)#retorna o range do index
print(df.sort_values(by='col1')) #coloca a coluna que foi passado por parametro fique ordenado
print(df.isnull)#retorna dentro do dataframe quem é nulo
print(df.dropna)#remove os valores Nan
print('--'*40)
data = {'A':['foo','foo','foo','bar','bar','bar'],
        'B':['one','one','two','two','one','one'],
        'C':['x','y','x','y','x','y'],
        'D':[1,3,2,5,4,1]}
df = pd.DataFrame(data)
print('--'*40)
print(df.pivot_table(values='D',index=['A','B'],columns=['C']))
import pandas as pd
#Criando um DataFrame
data = {'Empresa':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
        'Nome':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
        'Venda': [200,120,340,124,243,350]}
df = pd.DataFrame(data)
print(df)
print('--'*40)
group = df.groupby('Empresa') #Agrupando por empresa.
print(group.sum()) #Vendo o total de venda de cada empresa.
print(group.mean())#mediia de cada empresa
print(group.describe())#retorna uma serie de metdos pre aplicados e retorna um relatorio
print('--'*40)
group = df.groupby('Nome') #Agrupando pela tabela Nome
print(group.sum()) #Vendo o total de venda de cada integrante
print('--'*40)
print(group.sum().loc['Charlie'])#Vendo o total de vendas de um determinado vendedor, passar o nome do vendedor como parametro
print('--'*40)

import pandas as pd
import numpy as np
dicionario = {'A':[1,2,np.nan],'B':[5,np.nan,np.nan],'C':[1,2,3]}
print(dicionario)
print('--'*40)
df = pd.DataFrame(dicionario)
print(df)
print('--'*40)
print(df.dropna()) #elimina qualquer linha cuja a coluna tenha nulos
print('--'*40)
print(df.fillna(value="Fill na")) #substitui os valores nulos pelo que eu colocar no value
print('--'*40)
#substituindo a coluna A que tem um valor nulo pela media da coluna
print(df['A'].fillna(value=df['A'].mean()))
print('--'*40)
#preenchendo as lacunas nulas com dados registrados anteriormente
print(df.fillna(method='ffill'))
print('--'*40)




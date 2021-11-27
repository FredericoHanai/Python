import numpy as np
import pandas as pd

df = pd.read_csv(r'C:\Users\hanai\Downloads\Python\Python-Data-Science-and-Machine-Learning-Bootcamp\2. Python para análise de dados\Pandas\exemplo',sep=',') #colocando o 'r' antes da sring do caminho o python reconhece como Raw Format ai funciona.
print(df)
print('--'*40)
df = df +1
print(df)#somando 1 para todos os valores do dataframe
print('--'*40)
#exportando dados que usamos e trabalhamos dentro do Data Frame
df.to_csv("exemplo.csv",sep=';',decimal=',')
df = pd.read_html('https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/')
print(df[0])
import numpy as np
import pandas as pd

#niveis de indice
outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index) #a Funcao 'zip' retorna uma lista de tuplas, onde a i-ésima tupla contem o i-ésimo elemento de cada um dos argumentos

df = pd.DataFrame(np.random.randn(6,2),index=hier_index,columns=['A','B'])
df.index.names = ['Grupo', 'Numero'] #renomeando o indice G1 como grupo e os numeros como numero
print(df.xs(1,level='Numero')) #printando a sessao do G1 usando o xs, vantagem de usar o xs e nao o loc: pegar o valor sem ter que ir passando por niveis pra acessar o valor

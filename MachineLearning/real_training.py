import numpy as np
import pandas as pd
np.random.seed(101)
df = pd.DataFrame(np.random.randn(5,4),index='A B C D E'.split(),columns='W X Y Z'.split())
print(df)
print('--'*40)
print(df.loc[['C','D'],['X','Y']])
print(df.iloc[2:4,1:3])

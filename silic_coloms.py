import pandas as pd
import numpy as np

#thema: membalik urutan baris

n_rows = 5
n_cols = 5
cols = tuple('ABCDE') # 2 coloms
df = pd.DataFrame(np.random.randint(1, 10, size=(n_rows, n_cols)),
                  columns=cols)
print(df)

print("="*100)
# me-refrese kolom
df_l = df.loc[:, ::-1] #loc[menandakan baris/index, menandakan kolom]
print(df_l)

print("="*100)
# baris
df_b = df.loc[::-1,]
print(df_b)

import pandas as pd
import numpy as np

n_rows = 5
n_cols = 5
cols = tuple('ABCDE')
df = pd.DataFrame(np.random.randint(1,20, size=(n_rows, n_cols)), columns=cols)
print(df)

print("="*100)
# membagi df
df1 = df.copy(deep=True)
df1 = df1.drop([1,4])
print(df1)

df2 = df.copy(deep=True)
df2 = df2.drop([0,3])
print(df2)

print("="*100)
# menggabungkan dua df di atas
df_inner = pd.merge(df1, df2, how='inner')
print(df_inner)
print("\n")
df_outer = pd.merge(df1, df2, how='outer')
print(df_outer)
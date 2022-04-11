import pandas as pd
import numpy as np

# materi kali ini: membagi dua dataframe

#makeDF
n_rows = 10
n_cols = 5
cols = tuple('ABCDE')

df = pd.DataFrame(np.random.randint(1, 20, size=(n_rows, n_cols)), columns=cols)
print(df)

print(df.shape)
#membagi
proporsi = 0.7 # 70%
df_1 = df.sample(frac=proporsi)
df_2 = df.drop(df_1.index)

print(f'df_1 shape: ', df_1.shape) # 70% buat df_1
print(f'df_2 shape: ', df_2.shape) # 30% buat df_2

print(df_1)
print("\n")
print(df_2)
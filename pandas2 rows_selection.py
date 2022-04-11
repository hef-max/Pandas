import pandas as pd
import numpy as np

# data frame
n_rows = 10
n_colms = 5
cols = tuple('ABCDE')
df = pd.DataFrame(np.random.randint(1, 5, size=(n_rows, n_colms)), columns=cols)
print(df)
print("="*100)

# selctions with logic \cara1
sc_df = df[(df['A'] == 1) | (df['A'] == 3)]
print(sc_df)

print("="*100)
# selection with isin() \cara2
sc_df_2 = df[df['A'].isin([1,3])]
print(sc_df_2)

print("="*100)

#operator negasi ~
# contoh dengan not / bukan dari 1,3
ng_sc_df = df[~df['A'].isin([1,3])]
print(ng_sc_df)
#jadi akan mengambil data yg bukan 1 dan 3

import pandas as pd
import numpy as np

n_rows = 5
n_cols = 5
cols = tuple('ABCDE') # 2 coloms
df = pd.DataFrame(np.random.randint(1, 10, size=(n_rows, n_cols)),
                  columns=cols)
print(df)

# mengubah satu coloms
df_hobi = df.rename(columns={'C':'Hobi'})
print(df_hobi)

# mengubah beberapa coloms
df_coloms = df.rename(columns={'A':'Nama', 'B':'Alamat', 'D':'Kota'})
print(df_coloms)

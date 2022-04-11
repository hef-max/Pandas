import pandas as pd
import numpy as np

# materi kali ini adalah: sleksi baris dan colom

n_rows = 10
n_cols = 5
coloms = tuple('ABCDE')
df = pd.DataFrame(np.random.randint(1,20, size=(n_rows, n_cols)), columns=coloms)
print(df)

print("="*100)
# seleksi
seleksi_df = df.loc[[0,3,4], ['B','E']] #.loc[[baris], [coloms]]
print(seleksi_df)

print('='*100)
# bisa juga dengan kondisi
with_kondisi = df.loc[df['B']>10, ['B', 'C', 'D']] #kondisi B nilainya harus lebih  10
print(with_kondisi)

print("="*100)
# with selaicing
selc_df = df.loc[ 0:4 ,'B':'D']
print(selc_df)
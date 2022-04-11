import pandas as pd
import numpy as np
import pandas.util.testing as pdut
# pemilihan kolom

n_rows = 5
n_cols = 2
cols = ['bil_pecahan', 'bil_bulat'] # 2 coloms
df = pd.DataFrame(np.random.randint(1, 20, size=(n_rows, n_cols)),
                  columns=cols)
df['bil_pecahan'] = df['bil_pecahan'].astype('float')

df.index = pdut.makeDateIndex(n_rows, freq='H')
df = df.reset_index()

df['teks'] = list('ABCDE') # meke coloms baru

print(df)


print("="*100)
print("memilih kolom bertipe data numeric")
print("="*100)
# memilih kolom bertipe data numeric

df_num = df.select_dtypes(include="number")
print(df_num)

df_f = df.select_dtypes(include='float')
print(df_f)

df_int = df.select_dtypes(include='int')
print(df_int)

# memilih tpdata string atau object
df_o = df.select_dtypes(include='object')
print(df_o)

df_dtime = df.select_dtypes(include='datetime')
print(df_dtime)


# bisa juga untuk mengambil 2 atau lebih     df.select.dtypes(include=['typedata', 'typedata'])


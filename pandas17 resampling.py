import pandas as pd
import numpy as np
import pandas.util.testing as pdut

# materi kali ini adalah tentang resampling dimana pahami saja


rows = 365 * 24 # artinya 365 hari/1 tahun x 1 jam
cols = 2
coloms = ['cols1', 'cols2']

df = pd.DataFrame(np.random.randint(1,20, size=(rows, cols)), columns=coloms)

df.index = pdut.makeDateIndex(rows, freq='H') # atau Hour
print(df)


print('='*100)

#===== proses resampling ======
# berdasarkan bulan dengan .resample('M') untuk Month
df_m = df.resample('M')['cols1'].sum().to_frame()
print(df_m)

print("\n")
# berdasarkan dayli
df_d = df.resample('D')['cols1'].sum().to_frame()
print(df_d)
import pandas as pd
import numpy as np
import pandas.util.testing as pdut
import IPython.display as display

rows = 5
cols = 2
coloms = ['omset', 'operasional']
df = pd.DataFrame(np.random.randint(1,20, size=(rows, cols)), columns=coloms)

print(df)

print("="*100)
# kita akan kalikan ke dalam 100.000 an
df['omset'] = df['omset'] * 100_000
df['operasional'] = df['operasional'] * 10_000
print(df)

print("="*100)
# kita akan menambahkan date/waktu
df.index = pdut.makeDateIndex(rows, freq='D')
df = df.reset_index()
df = df.rename(columns={'index':'tanggal'})
print(df)

print("="*100)
# nah baru kita msuk ke materinya yaitu formating
print("="*100)


coba = df.style.format('{:.2f}')

print(coba)

# ini masih error

# formatku = {'tanggal':'{:%d/%m/%y}',
#             'operasional':'Rp {:.2f}',
#             'omset':'Rp {:.2f}'
#             }

# laporan = df.style.format("{:.2f}")
# df.style.format({"omset": "{:.2f}", "operasional": "Rp{:.2f}"})



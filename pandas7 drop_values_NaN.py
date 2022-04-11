import pandas as pd

# materi kali ini: mendrop out missing value atau NaN

# make DataFrame
df = pd.util.testing.makeMissingDataframe().reset_index()
print(df.head())

print("="*100)

# rename index
df_z = df.rename(columns={'index': 'Z'})
print(df_z.head())

# make copy
df_backup = df_z.copy(deep=True)

print("="*100)
# mendrop NaN data in coloms
df_dropVM = df_z.dropna(axis='columns')
print(df_dropVM.head())

# medrop NaN in evry rows / in rows
df_b = df_backup.copy(deep=True)
df_d = df_b.dropna(axis='rows')
print(df_d.head())

print("="*100)
# presentase MV for every coloms
df_b1 = df_backup.copy(deep='True')
print(df_b1.isna().mean())

# mentoleran using treshold
treshold = len(df_b1) * 0.9 #atau 90%
df_th = df_b1.dropna(thresh=treshold, axis='columns')
print(df_th.head())


# AWAS .head() disini untuk mengambil data ke 5 saja

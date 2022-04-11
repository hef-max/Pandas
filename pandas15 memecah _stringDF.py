import pandas as pd

# materi kali ini adalah memecahkan nilai string di data frame

df = pd.DataFrame({'nama':['Hefry Anesti', 'Ramdhan Dianto', 'Ary Muhammad'],
                   'tempat_kelahiran':['Bongas, Indramayu', 'Bongas, Indramayu', 'Wanguk, Indramayu']}
                  )

# make new coloms
df[['nama_depan', 'nama_belakang']] = df['nama'].str.split(' ', expand=True) # df['nama'] kita mengambil dic
df[['kecamatan', 'kabupaten']] = df['tempat_kelahiran'].str.split(',', expand=True)

print(df)



print("="*100)
# latihan
print("latihan")

data = {'nama_anak':['rony', 'sony', 'roxy', 'sonya'],
        'nilai_anak':[73, 80, 75, 71]}
data_anak = pd.DataFrame(data)

data_anak.loc[data_anak['nilai_anak'] >= 73, 'kelulusan'] = 'lulus'
data_anak.loc[data_anak['nilai_anak'] < 73, 'kelulusan'] = 'gagal'

print(data_anak)

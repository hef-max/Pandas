import pandas as pd

# materi kali ini adalah menata ulang data frame dengan multiple index, pakai func unstack()

df = pd.read_csv('data/titanicfull.csv')
print(df.head())

print("="*100)
# mengelompokan data yg kita inginkan
df_grup = df.groupby(['sex', 'pclass'])['survived'].mean().to_frame() # .mean() untuk mengambil nilai rata"
print(df_grup)

print("="*100)

# supaya mudah dibaca dengan unstack()
df_grup1 = df.groupby(['sex', 'pclass'])['survived'].mean().unstack() # .mean() untuk mengambil nilai rata"
print(df_grup1)





# latihan =============================================================================
print("="*100)
print("latihan")

data = pd.read_csv('data/StudentsPerformance.csv')

# re = data.rename(index={"master's degree": "NEW NAME"}, inplace = False)

data_gp = data.groupby(['gender', 'parental level of education'])['math score'].mean().unstack()
print(data_gp)




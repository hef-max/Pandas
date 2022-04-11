import pandas as pd

#make data frame
df = pd.read_csv('data/titanicfull.csv')
df.columns = ['Pclass', 'Survival status', 'full Name', 'Sex ', ' Age',
              'Sib SP', 'parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']

df_backup = df.copy(deep=True)
print(df.head())

print("="*150)

df.columns = df.columns.str.replace(' ', '_').str.lower()
print(df.head())

print("="*150)

df_backup = df_backup.copy(deep=True)
df.columns = df.columns.str.lower().str.strip().str.replace(' ', '_')
print(df.head())
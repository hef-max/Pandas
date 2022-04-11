import pandas as pd
import numpy as np

# data frame
data = {'cols1': ['1', '2', '3', 'teks'],
        'cols2': ['1', '2', '3', '4']}
df = pd.DataFrame(data)
print(df)
print(df.dtypes)

print("="*100)

# merubah object ke int\float or lain
df_x = df.astype({'cols2': 'int'})
print(df_x.dtypes)

print("="*100)

# to numeric
df_n = df.apply(pd.to_numeric, errors='coerce') #with change parameter error
print(df_n)

df_c = df_n[~df_n['cols1'].isin([np.nan])]
print(df_c)
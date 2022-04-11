import pandas as pd
import numpy as np

n_rows = 10
n_cols = 1
cols = ('usia', )
df = pd.DataFrame(np.random.randint(1,90, size=(n_rows, n_cols)), columns=cols)
print(df)

print("="*100)
# cara menkonversi / pengelompkan
df['kelompok_usia'] = pd.cut(df['usia'], bins= [0, 10, 25, 65, 90],
                             labels=['anak', 'remaja', 'dewasa', 'manula'])

print(df)


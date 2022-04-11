import pandas as pd
import numpy as np

# data frame
n_rows = 5
n_colms = 5
cols = tuple('ABCDE')
df = pd.DataFrame(np.random.randint(1, 10, size=(n_rows, n_colms)), columns=cols)

print(df)

print("="*100)

# prefix
df_prefix = df.add_prefix('kolom_')
print(df_prefix)

# suffix
df_suffix = df.add_suffix('_field')
print(df_suffix)
import pandas as pd
import numpy as np

data = {'day':  [1, 2, 10, 15, 20],
        'month':    [1, 3, 5, 6, 8],
        'Year': [2002, 2006, 2009, 2015, 2020]
        }

df = pd.DataFrame(data)
print(df)

print("="*100)
# membentuk data datetime
df["penanggalan"] = pd.to_datetime(df[data])
print(df)
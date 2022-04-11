import pandas as pd
import numpy as np

# materi kali ini adalah: series untuk find kesamaan kolom
# series itu seperti colom

# make data
data = {'A': [15, 15, 18, np.nan, 12],
        'B': [15, 15, 18, np.nan, 12]
        }
df = pd.DataFrame(data)
print(df)

print(df['A']) # satau series

print("="*100)
# memeriksa kesamaan dengan oper == /cara 1
print(df['A'] == df['B'])

print("\n")
# memeriksa dengan equels() /cara2
print(df['A'].equals(df['B']))


# AWAS JIKA KITA INGIN MEMBANDINGKAN DF DON'T USING == BUT .equals()
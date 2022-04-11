import pandas as pd
import numpy as np

data = pd.read_csv('../data/Mall_Customers.csv')
df = pd.DataFrame(data, columns=['Genre', 'Age'])


for key in df:
    print(df[key]['Age'])


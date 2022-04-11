import pandas as pd
import numpy as np
import pandas.util.testing as pdut

# materi kali ini tentang dummy DF adalah bebrapa cara membuat DF

# cara 1
# menggunakan dic
cara1 = pd.DataFrame({'cols1':[1,2,3,4],
                      'cols2':[5,6,7,8]})
print(cara1)


print("="*100)

# cara 2
# with numpy
rows = 5
cols = 3
array = np.random.randint(1, 20, size=(rows, cols))
cara2 = pd.DataFrame(array, columns=tuple('ABC'))
print(cara2)

print("="*100)

# cara 3
# with util.testing
cara3 = pdut.makeDataFrame().head() # dengan nilai acak
print(cara3)

cara3_1 = pdut.makeMixedDataFrame().head() # yg tipe data campur
print(cara3_1)

cara3_2 = pdut.makeTimeDataFrame().head() # dengan waktu
print(cara3_2)

cara3_3 = pdut.makeMissingDataframe().head() # dengan missing value or NaN
print(cara3_3)
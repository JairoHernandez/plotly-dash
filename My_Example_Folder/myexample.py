import numpy as np
import pandas as pd

mat = np.arange(0,10).reshape(5,2)
print(mat)
df = pd.DataFrame(data=mat, columns=['A', 'B'])
print('====')
print(df)

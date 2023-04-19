import pandas as pd
# import numpy as np
import math
print(".......execution started.....")
df2= pd.read_csv('/Users/aakashsharma/Desktop/bni/bq-main.csv')

df2.head()
rows=len(df2)
print(rows, "rows")
from math import ceil

number_of_files = ceil(rows/6000000)
print(number_of_files)
rows = len(df2)
size = 6000000

k = ceil(rows / size)

for i in range(k):
    df = df2[size * i:size * (i + 1)]
    df.to_csv(f'/Users/aakashsharma/Desktop/bni/bni_data_{i + 1}.csv', index=False)
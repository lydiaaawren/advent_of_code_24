import pandas as pd
import numpy as np

df = pd.read_csv('day2.txt', header=None, sep=' ')

j = 0
value = []

while j < 1000:
    i=1
    direction=[]
    size=[]
    row=df.loc[j,:]
    row=row.head(np.count_nonzero(~np.isnan(row)))
    while i < len(row):
        direction.append(np.sign(row[i-1]-row[i]))
        if abs(row[i-1]-row[i]) <= 3 and abs(row[i-1]-row[i]) >= 1:
            size.append(1)
        i+=1
    if abs(sum(direction)) == len(row) - 1 and sum(size) == len(row) - 1:
        value.append(j)
    j += 1

print(len(value))

for v in value:
    df = df.drop([v])

passed=0
k=0

while k < len(df):
    row=df.loc[k,:]
    row=row.head(np.count_nonzero(~np.isnan(row)))
    j=0
    level_passed=0
    while j < len(row):
        adjusted_row = row.drop([j])
        direction = []
        size = []
        i = 0
        ls = list(range(len(row)))
        ls.remove(j)
        while i < len(ls)-1:
            direction.append(int(np.sign(adjusted_row[ls[i]]-adjusted_row[ls[i+1]])))
            if abs(adjusted_row[ls[i]]-adjusted_row[ls[i+1]]) <= 3 and abs(adjusted_row[ls[i]]-adjusted_row[ls[i+1]]) >= 1:
                size.append(1)
            i += 1
        if abs(sum(direction)) == len(adjusted_row) - 1 and sum(size) == len(adjusted_row) - 1:
            level_passed+=1
        j+=1
    if level_passed >= 1:
        passed+=1
    k+=1

print(passed)

print(passed+len(value))

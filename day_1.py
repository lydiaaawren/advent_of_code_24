import pandas as pd

df = pd.read_csv('input.txt', sep='   ', header=None)

list1 = list(df[0])
list1.sort()

list2 = list(df[1])
list2.sort()

df[0]=pd.array(list1)
df[1]=pd.array(list2)

df[2] = abs(df[0]-df[1])

print('the difference is', sum(df[2]))

similarity = 0

for i in df[0]:
    multiplier = 0
    for j in df[1]:
        if i == j:
            multiplier += 1
    similarity += i*multiplier

print('similarity score is', similarity)

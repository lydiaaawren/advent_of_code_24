# day 3

import re

txt = open('day3.txt', 'r').read()

xs = re.findall('mul\(\d+,\d+\)',txt)

value = 0

for i in range(len(xs)):
    z = []
    x = xs[i]
    ys = re.split(',', x)
    z.append(re.sub('mul\(', '', ys[0]))
    z.append(re.sub('\)', '', ys[1]))
    value += int(z[0])*int(z[1])

print(value)

alldos = re.split('do', txt)

do = []
dont = []

for a in alldos:
    if re.search("^n't",a):
        dont.append(a)
    else:
        do.append(a)


list_of_mul_lists = []

for d in do:
    list_of_mul_lists.append(re.findall('mul\(\d+,\d+\)',d))

value = 0

for l in list_of_mul_lists:

    active_list = l

    for i in range(len(active_list)):
        x = active_list[i]
        ys = re.split(',', x)
        value += int(re.sub('\)', '', ys[1]))*int(re.sub('mul\(', '', ys[0]))

print(value)

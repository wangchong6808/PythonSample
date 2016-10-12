basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
print('orange' in basket)
print(basket.__contains__('apple'))

# set comprehensions
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)

list = ["yellow", "blue", "black", "green", "blue"]
sets = set(list)
for i, v in enumerate(sets) :
    print(i, v);


import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)
print(filtered_data)

print('CABD' < 'C')


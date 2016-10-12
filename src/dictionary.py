tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127

keys = sorted(tel.keys())
print(keys)

for key in keys :
    print(key, tel.get(key))

dic = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
dic = dict(sape=4139, guido=4127, jack=4098)
dic = {x: x**2 for x in (2, 4, 6)}

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i ,v)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
     print('What is your {0}?  It is {1}.'.format(q, a))

for i in reversed(range(1, 10, 2)):
     print(i)
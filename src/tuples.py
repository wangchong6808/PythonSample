# define a tuple with single element
singleton = 'hello',
t = 12345, 54321, 'hello!'
t = (12345, 54321, 'hello!')
# unpacking tuple into multiple variables
x, y, z = t
print(len(singleton))
print(t)
print(x)

t = (x**2 for x in range(1,10))
for tt in t :
    print(tt, end=" ")

print(list(range(1,10)))

from my_functions import add

def add(x, y) :
    return x + y +10


print(add(1,22))
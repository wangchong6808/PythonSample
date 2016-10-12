a, b = 0, 1
while b < 10:
     print(a, b)
     a, b = b, a+b


x = 1 #int(input("Please enter an integer: "))
if x < 0:
     x = 0
     print('Negative changed to zero')
elif x == 0:
     print('Zero')
elif x == 1:
     print('Single')
else:
     print('More')


words = ['cat', 'window', 'defenestrate']
for w in words:
     print(w, len(w))

for i in range(5):
     print(i)

for i in range(0, 10, 3):
    print(i)

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

a= list(range(5))
for i in a:
    print(i)
print("------------------------")
for n in range(2, 10):
     for x in range(2, n):
         if n % x == 0:
             print(n, 'equals', x, '*', n//x)
             break
         else:
             # loop fell through without finding a factor
             print(n, 'is a prime number')
print('--------------------------')
# loop’s else clause runs when no break occurs
for n in range(2, 10):
     for x in range(2, n):
         if n % x == 0:
             print(n, 'equals', x, '*', n//x)
             break
     else:
         # loop fell through without finding a factor
         print(n, 'is a prime number')


for num in range(2, 10):
     if num % 2 == 0:
         print("Found an even number", num)
         continue
     print("Found a odd number", num)



class MyEmptyClass:
     pass
squares = [1, 4, 9, 16, 25]
squares.append(36);
print(squares)
print(squares[1])
print(squares[-3:])

# return a new copy of the list
sq = squares[:]
squares.append(49)
print(sq)

squares = squares + [36, 49, 64, 81, 100]
print(squares)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters[2:5] = ['C', 'D', 'E']
print(letters)
print(letters[2:5])
letters[2:5] = []
print(letters)
letters = 12;
print(letters)

original=[1,2,3]
original[len(original):]=[4,5]
print(original[2:])
original.extend([6,7,8])
print(original)
print(original.pop(0))
print(original.pop())
original.sort(reverse=True)

from collections import deque

print(original)

queue = deque(["Eric", "John", "Michael"])
print(queue.popleft())

#  list comprehensions
compre = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(compre)

matrix = [
     [1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
 ]

list = [[row[i] for row in matrix] for i in range(4)]
print(list)
del list[2:4]
print(list)


# unpacking a list into multiple variables
m,n = list
print(m)
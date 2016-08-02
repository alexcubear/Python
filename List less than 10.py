import random

num = int(input("Enter your number: "))
x = []
a = []

for i in range(0,10):
    x.append(random.randrange(0, 100))

for element in x:
    if element < num:
        a.append(element)

print(a)

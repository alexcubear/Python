import random

a = random.sample(range(1, 50), random.randrange(10, 20))
b = random.sample(range(1,50), random.randrange(10, 20))

newlist = [i for i in a if i in b]

print(newlist)
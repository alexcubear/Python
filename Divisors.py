num = int(input('Enter your number: '))

listdivisors = []
for elem in range(1, num+1):
    if num % elem == 0:
        listdivisors.append(elem)

print(listdivisors)

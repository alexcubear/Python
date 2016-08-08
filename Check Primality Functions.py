num = int(input('Enter your number: '))
a = [x for x in range(2, num) if num % x == 0]

if num > 1:
    if len(a) == 0:
        print('Your number is prime.')
    else:
        print('Your number is not prime.')
else:
    print('Your number is not prime.')




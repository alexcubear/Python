import random

comp = random.randrange(0, 9)
user = 0

print('Computer has generated an unknown number. Try to guess it!')

while comp != user and user != 'exit':
    user = input('Enter your number: ')
    if str(user).lower() != 'exit':
        if int(user) == comp:
            print('You have guessed the number!')
            break
        elif int(user) > comp:
            print('Your number is higher than computer\'s')
        elif int(user) < comp:
            print('Your number is less than computer\'s')

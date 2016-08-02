num = int(input('Enter a number: '))
check = int(input('Enter one more number: '))
mod = num % 2

def oddoreven():
    if num % 4 == 0:
        print(num, 'is a multiple of 4')
    elif num % 2 == 0:
        print(num, 'is an even number')
    else:
        print(num, 'is an odd number')


    if num % check == 0:
        print(num, 'divides evenly by', check)
    else:
        print(num, 'doesn\'t divide evenly by', check)


oddoreven()
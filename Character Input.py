from datetime import date

curyear = date.today().year
uname = input('Enter your name: ')
uage = int(input('Enter your age: '))
msg = uname + ', you will be 100 in ' + str((curyear - int(uage) + 100))
print(msg)

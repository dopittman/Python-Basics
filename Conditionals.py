
# Examples of how to utilize conditionals in Python

def ifs_in_python(num):
    if num > 10:
        print('Your number is greater than 10')
    elif num >= 2:
        print('Your number is between 2 and 10')
    elif num == 1 or num == 0:
        print('Your number is either 1 or 0')
    else:
        print('Your number is a negative number')


myNumber = input("Enter your favorite number: ")
ifs_in_python(int(myNumber))

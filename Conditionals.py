
# Examples of how to utilize conditionals in Python

# if and elif example w/ 'or' conditional
def ifs_in_python(num):
    if num > 10:
        print('Your number is greater than 10')
    elif num >= 2:
        print('Your number is between 2 and 10')
    elif num == 1 or num == 0:
        print('Your number is either 1 or 0')
    else:
        print('Your number is a negative number')

# 'is' vs '=='
# 'is' basically checks if the variables exists in the same place in memory
# where '==' checks if the variables have the same values
example = 1
example == 1 # True
example is 1 # True

a = [1, 2, 3]
b = [1, 2, 3]
a == b # True
a is b # False
c = b
b is c # True


myNumber = input("Enter your favorite number: ")
ifs_in_python(int(myNumber))

# basic function example
def hello():
    print('Howdy!')
    print('Howdy!!')
    print('Hello there!')

hello()
hello()
hello()
# each time you call the function, it starts at the top and runs though the whole function (unless told otherwise)

# passing arguments to functions to be used as a parameter in the function
def hi(name):
    print('Hello ' + name)

hi('Frank')
hi('Bob')

# another example of passing an argument to the function and storing the return into a variable
def plusOne(number):
    return number + 1

newNumber = plusOne(5)
print(newNumber)

# example of changing 'end' keyword argument on the print fuction
print('Hello', end='')
print('World')
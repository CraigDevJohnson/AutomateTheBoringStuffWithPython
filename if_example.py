# if examples
# Basic if name is Alice
name = 'Alice'
if name == 'Alice':
    print('Hi, ' + name + '!')
else:
    print('Oh, I was expecting Alice... Still nice to met you ' + name + '!')
print('Done')

# Basic if name isn't Alice
name = 'Bob'
if name == 'Alice':
    print('Hi, ' + name + '!')
else:
    print('Well, hello there ' + name + '!')
print('Done')

# Basic else if statement
name = 'Bob'
if name == 'Alice':
    print('Hi, ' + name + '!')
elif name == 'Bob':
    print('Hi there, ' + name + '!')
else:
    print('Well, hello there ' + name + '!')
print('Done')

# Truthy value
print('Enter a name please:')
name = input()
if name:
    print('Thank you fer entering your name, ' + name + '!')
else:
    print('You did not enter a name... Rude!')

# Better to be more explicit
print('Enter a name please:')
name = input()
if name != '':
    print('Thank you fer entering your name, ' + name + '!')
else:
    print('You did not enter a name... Rude!')
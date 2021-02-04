spam = [1,2,3]
cheese = spam
cheese.append('Hello')
print(cheese)
print(spam)

# Even though we are acting in the function's local scope, it is referencing a global object and is therefore making that change in the global scope
# This is the equivalent to the above code
def eggs(someParameter):
    someParameter.append('Hello')
    print(someParameter)

spam = [1,2,3]
eggs(spam)
print(spam)

# use the copy module to make a copy of the list rather than a second reference if you need them to be separated
import copy
spam = [1,2,3]
cheese = copy.deepcopy(spam)
cheese.append('Hello')
print(cheese)
print(spam)

# lists will cause python to ignore line indentation for readibility sake
spam = ['apples',
        'oranges',
        'bananas',
        'cats']

# you can force python to ignore line indentation by useing \ as well
print('Four score and seven ' + \
        'years ago')
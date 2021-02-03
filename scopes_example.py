spam = 42 # global variable/scope - created when a program is ran and destroyed when it ends

def eggs():
    spam = 42 # local variable/scope - created when a function is called and destroyed/lost when it returns

print('Some code here.')
print('some more code.')

# 1. Code in global scope annot use any local variables.
def spam():
    eggs = 99

spam()
# below print errors because there is no global variable name eggs to return cause it was destroyed after the fucntion ran
print(eggs)

# 2. Code in one fucntion's local scope cannot use variables in any other local scope.
def spam():
    eggs = 99
    bacon()
    print(eggs)

def bacon():
    ham = 101
    eggs = 0
# looking at it, you would expect spam to print 0 but eggs = 0 only exists in the bacon function, so the last declaration is 99 in spam.
spam()

# 3. Code in a local scope can access global variable.
def spam():
    print(eggs)
    
eggs = 0
# first it checks for eggs local variable (an assignment statement), sees there isn't one (no assignment statement), and prints out the global veariable.
spam()

def spam():
    eggs = 'Hello'
    # since there is an assignment statement, it knows to use the local variable eggs instead of the global one.
    print(eggs)
    
eggs = 0
spam()
# now that we are out of the function's local scope, it uses the global variable eggs in the print function
print(eggs)

def spam():
    global eggs # this tells python that within this function, eggs is referring to the global variable and will set the global variable to any assignment statement in the fucntion
    eggs = 'Hello'
    # since there is an assignment statement, it knows to use the local variable eggs instead of the global one.
    print(eggs)
    
spam()
print(eggs)
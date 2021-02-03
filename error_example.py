# example of error handling
def div42by(divideBy):
    return 42 / divideBy

print(div42by(2))
print(div42by(12))
# can't devide by 0, so will error
#print(div42by(0))
print(div42by(1))

# example of error handling
def div42by(divideBy):
    # if it runs into a ZeroDivisionError error running the code in the try block, then run the code in the except block 
    # (can leave as just except: to have it catch all errors)
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: You tried to divide by zero!')

print(div42by(2))
print(div42by(12))
# can't devide by 0, so will error
print(div42by(0))
print(div42by(1))

print('How many cats do you have?')
numCats = input()
try:
    if int(numCats) >= 4:
        print('That is a lot of cats.')
    elif int(numCats) < 0:
        print('You can\'t have negative cats!')
    else:
        print('That is not that many cats.')
except ValueError:
    print('You did not enter an integer')
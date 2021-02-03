spam = 0
while spam < 5:
    print('Hello!')
    spam = spam + 1

# verifying variables (but be careful of what you are checking for)
name = ''
while name != 'your name':
    print('Please type "your name".')
    name = input()
print ('Thank you!')

# using break to exit loop
name = ''
while True:
    print('Please type "your name".')
    name = input()
    if name == 'your name':
        break
print ('Thank you!')

# example of continue (which will stop and jump back to the start of while loop)
spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue
    print('spam is ' + str(spam))
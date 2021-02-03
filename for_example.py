# basic for loop
print('My name is')
for i in range(5):
    print('Jimmy Five Times ' + str(i))

# while loop subbed out for for loop
print('My name is')
i = 0
while i < 5:
    print('Jimmy Five Times ' + str(i))
    i = i + 1


total = 0
for num in range(101):
    total = total + num
print(total)

# starting mid range, first number is where to start and second is to stop (but not include)
print('My name is')
for i in range(12,16):
    print('Jimmy Five Times ' + str(i))

# starting mid range, first number is where to start and second is to stop (but not include), thrid number is how many to incriment
print('My name is')
for i in range(12,30,2):
    print('Jimmy Five Times ' + str(i))
# Says Hello, asks name, asks age and returns random trivia

print("Hello, what is your name?")
myName = input()
print('It is great to meet you ' + myName + '!')
print('Your name is ' + str(len(myName)) + ' characters long.')
print('What is your age, if you don\'t mind me asking?')
myAge = input()
print('Thanks, you shouldn\'t date anyone younger than ' + str((int(myAge)) / 2 + 7) + '.')
print('Have a great day ' + myName +'!')
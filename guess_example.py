# This is a guess the number game.
import random

print('Hello! What is your name?')
name = input()

print('Well, ' + name + ', I am thinking of a number between 1 and 100... Can you guess it within 10 tries?')
secretNumber = random.randint(1,100)

# comment out below line when done debugging
print('DEBUG: Secret number is ' + str(secretNumber))
# use a switch function to get which guess they are on.
guessesUsed = 0
for guessesTaken in range(1,11):
    guessesUsed = guessesUsed + 1
    def guessesUsedString(i):
        switcher = {
                1:'First',
                2:'Second',
                3:'Third',
                4:'Fourth',
                5:'Fifth',
                6:'Sixth',
                7:'Seventh',
                8:'Eight',
                9:'Ninth',
                10:'Tenth and final'
            }
        return switcher.get(i)

    print('Take your ' + str(guessesUsedString(guessesUsed)) + ' guess!')
    try:
        guess = int(input())
        if guess < secretNumber:
            print('Your guess is too low!')
        elif guess > secretNumber:
            print('Your guess is too high!')
        else:
            break # This means they guess correctly
    except ValueError:
        print('Sorry, you need to only enter integers. Don\'t waste another guess!')

if guess == secretNumber:
    print('Great job ' + name + '! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('You reached 10 guesses. The number I was thinking of was ' + str(secretNumber) + '!')

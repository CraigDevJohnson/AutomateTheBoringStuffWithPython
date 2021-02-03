
# import the sys module and then call the exit function to exit the script before it finishes running
import sys, pyperclip
pyperclip.copy('Hello world!')
pyperclip.paste()
print('Hello')
sys.exit()
print('Goodbye')
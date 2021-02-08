#! python3

import re,pyperclip

# Create a regex for phone numbers
phoneRegex = re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 123456, x12345
# area code (option)
(
((\d\d\d)|(\(\d\d\d))?
# first separator
(\s|-)
# first 3 digits
\d\d\d
# second separator
-
# last 4 digits
\d\d\d\d
# extension word part (optional)
(((ext(\.)?\s)|x)
# extension digits
(\d{2,5}))?
)
''', re.VERBOSE)

# Create a regex for email address
emailRegex = re.compile(r'''
# some.+_thing@something.com
# name part
[a-zA-Z0-9_.+]+
# @ symbol
@
# domain name part
[a-zA-Z0-9_.+]+
''', re.VERBOSE)

# Get the text off the clipboard
text = pyperclip.paste()

# Extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)
allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

# TODO: Copy the extracted email/phone to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)
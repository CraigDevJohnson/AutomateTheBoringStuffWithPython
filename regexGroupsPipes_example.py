import re
# use () to separate groups in the regex so you can call specific parts of the regex
phoneNumbRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumbRegex.search('My number is 415-555-4242')
print('Phone number has aread code of ' + mo.group(1) + ' and number of ' + mo.group(2))

# if looking for a () then need to escape in the regex with \
phoneNumbRegex = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
mo = phoneNumbRegex.search('My number is (415) 555-4242')
print(mo.group())

# use pipes to search for variations
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())


mo = batRegex.search('Batmotorcyle lost a wheel')
print(mo == None)
# note if search can't find it, it returns none, so you can't just blindly assign it or you'll get errors
# print(mo.group())   <- this would error

# select the second group to identify which variation it found
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group(1))
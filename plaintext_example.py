import os,shelve
helloFile = open('/home/cjohnson/hello.txt')
content = helloFile.read()
print(content)
helloFile.close()

helloFile = open('/home/cjohnson/hello.txt')
print(helloFile.readlines())
helloFile.close()

helloFile = open('/home/cjohnson/hello2.txt', 'w')
helloFile.write('Hello!!!!')
helloFile.close()

helloFile = open('/home/cjohnson/hello2.txt')
content = helloFile.read()
print(content)
helloFile.close()

baconFile = open('bacon.txt', 'a')
baconFile.write('Bacon is not a vege!\n')
baconFile = open('bacon.txt')
content = baconFile.read()
print(content)
baconFile.close()

shelfFile = shelve.open('mydata')
shelfFile['cats'] = ['Zaboo', 'Io', 'Pus']
shelfFile.close()
shelfFile = shelve.open('mydata')
print(shelfFile['cats'])
shelfFile.close()

shelfFile = shelve.open('mydata')
print(list(shelfFile.keys()))
print(list(shelfFile.values()))
shelfFile.close()

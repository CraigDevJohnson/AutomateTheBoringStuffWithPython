import os
totalSize = 0
for filename in os.listdir('/home/cjohnson'):
    if not os.path.isfile(os.path.join('/home/cjohnson', filename)):
        continue
    totalSize = totalSize + os.path.getsize(os.path.join('/home/cjohnson', filename))
print(totalSize)
import os
for folderName, subFolders, fileNames in os.walk(os.getcwd()):
    print('The folder is ' + folderName)
    if subFolders:
        print('The subfolders in ' +folderName + ' are: ' + str(subFolders))
    if fileNames:
        print('The file names in ' +folderName + ' are: ' + str(fileNames))
    print()

    for subFolder in subFolders:
        if 'fish' in subFolder:
            print(subFolder)

    for fileName in fileNames:
        if fileName.endswith('.py'):
            print(fileName)

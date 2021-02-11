def boxPrint(symbol, width, height):
    if len(symbol) !=1:
        raise Exception('"symbol" needs to be length 1')
    if (width < 2) or (height <2):
        raise Exception('width and/or height bust be greater than 1')
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)


boxPrint('*', 15, 10)

import traceback
try:
    raise Exception('This is an error message')
except:
    errorFile = open('error_log.txt', 'a')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written to error_log.txt')
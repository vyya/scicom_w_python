box = input('Enter a file name: ')
try:
    with open(box) as fhand:
        for line in fhand:
            line = line.rstrip()
            print(line.upper())
except:
     print('There is no file: ', box)
     quit() 

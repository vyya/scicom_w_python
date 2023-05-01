box = input('Enter a file name: ')
try:
    fhand = open(box)
except:
     print('There is no file: ', box)
     quit() 
for line in fhand:
    line = line.rstrip()
    print(line.upper())

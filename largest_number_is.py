largest = None
print('Before', largest)
for value in [11, 21, 32, 54, 15, 25, 78, 7]:
    if largest is None:
        largest = value
    elif largest < value:
        largest = value
    print(value, largest)
print('After', largest)

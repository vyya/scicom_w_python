smallest = None
print('Before', smallest)
for value in [6, 54, 32, 3, 87, 109, 87]:
    if smallest == None:
        smallest = value
    elif smallest > value:
        smallest = value
    print(value, smallest)
print('After', smallest)



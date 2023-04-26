count = 0
total = 0
while True:
    number = input('Enter a number: ')
    if number == 'done':
        break
    else:
        try:
            count += 1
            total += int(number)
        except:
            print('Invalid input')
            continue
print(count, total, total/count)
print('done')


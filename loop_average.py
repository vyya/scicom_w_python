count = 0
sum = 0
print('Before', count, sum)
for value in [76, 21, 6, 97, 2, 11, 65]:
    count += 1
    sum += value
    print(count, sum, value)
print('After', count, sum, sum/count)



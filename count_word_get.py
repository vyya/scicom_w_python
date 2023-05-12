name = input('Enter file: ')
handle = open(name)
counts =dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print('Number of words fox: ', counts.get('fox', 0))
print('Number of every word as dictionary: ', counts)
'''bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word 
        bigcount = count
print(bigword, bigcount)'''
tmp = list()
for word, count in counts.items():
    tmp.append((count, word))
tmp = sorted(tmp, reverse=True)
print(f"Here is the descending word frequency in a given text: {tmp}")

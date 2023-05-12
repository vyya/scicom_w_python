import re
x ='My 2 favorite numbers are 45 and 87.'
y = re.findall('[0-9]+', x) # extract one or more numbers in range 0-9 from the string x
print(y)
y = re.findall('[AEOU]+', x) # extracting one or more uppercase letters from the set
print(y) # empty string output
x = 'From: Using the : character'
y = re.findall('^F+:', x) # greedy search
print(y)
y = re.findall('^F+?:', x) # non-greedy search
print(y)
x = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('\S+@\S+', x) # \S - at least one non-whitespace charachter
print(y)
y = re.findall('^From (\S+@\S+'), x) # find From but extracting embraced only regexp
print(y)

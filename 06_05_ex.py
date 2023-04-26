str = 'X-DSPAM-Confidence: 0.8475 '
first = str.find(':')
print(first)
part = str[first + 1 : ]
print(part)
flt = float(part)
print(flt)

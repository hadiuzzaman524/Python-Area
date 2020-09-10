string = 'X-DSPAM-Confidence:0.8475'
index = string.find(':')
value=string[index+1:]
print(float(value))
print(string.replace('X','Bangla'))

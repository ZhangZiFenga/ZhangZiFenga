str='X-DSPAM-Confidence: 0.8475'
a=str.find(' ')
print(a)
num=str[a+1:]
print(num)
print(type(num))
print(type(float(num)))
from collections import defaultdict

str = input("please input a string:")

str = str.lower()

chars = defaultdict(int)

for char in str:
	chars[char]+=1
print(chars)
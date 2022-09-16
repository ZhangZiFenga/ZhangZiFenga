from collections import defaultdict
str = input("Please input a string：")
str = str.lower()
chars  = defaultdict(int)
for char in str:
    char[char] +=1
new chars = sorted(chars.items(), ket=lambda d:d[1],reverse=Ture)
print(new_chars)
s1 = input().strip()
s2 = input().strip()

str1 = s1.lower()
str2 = s2.lower()

ans = 0

for i in range(len(str1)):
    if ord(str1[i]) > ord(str2[i]):
        ans = 1
        break
    elif ord(str1[i]) < ord(str2[i]):
        ans = -1
        break

print(ans)
```[cite: 17]

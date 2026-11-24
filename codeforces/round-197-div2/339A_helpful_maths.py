s = input().strip()
digits = []

for i in range(0, len(s), 2):
    digits.append(s[i])

digits.sort()
print("+".join(digits))
```[cite: 17]

n = int(input().strip())

for _ in range(n):
    word = input().strip()
    s = word.lower()
    if len(s) > 10:
        first = s[0]
        last = s[-1]
        between = len(s) - 2
        print(str(first) + str(between) + str(last))
    else:
        print(s)
```[cite: 17]

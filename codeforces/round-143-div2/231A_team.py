n = int(input().strip())
count = 0

for _ in range(n):
    a, b, c = map(int, input().split())
    if (a == 1 and b == 1) or (b == 1 and c == 1) or (c == 1 and a == 1):
        count += 1

print(count)
```[cite: 14]

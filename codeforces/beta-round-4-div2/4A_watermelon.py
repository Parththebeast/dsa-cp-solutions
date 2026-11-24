n = int(input().strip())
count = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i % 2 == 0 and j % 2 == 0 and i + j == n:
            count += 1

if count > 0:
    print("YES")
else:
    print("NO")
```[cite: 16]

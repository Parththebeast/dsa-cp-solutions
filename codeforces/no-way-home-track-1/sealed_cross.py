n = int(input().strip())

for i in range(1, n + 1):
    row = []
    for j in range(1, n + 1):
        if i == j or i + j == n + 1:
            row.append("1")
        else:
            row.append("0")
    print(" ".join(row))
```[cite: 14]

n = int(input().strip())

for i in range(1, n + 1):
    if i == 1 or i == n:
        row = ""
        for j in range(n):
            row += "*"
        print(row)
    else:
        row = ""
        for j in range(1, n + 1):
            if j == 1 or j == n:
                row += "*"
            else:
                row += "."
        print(row)
```[cite: 13]

ci = 0
cj = 0

for i in range(5):
    row = list(map(int, input().split()))
    for j in range(5):
        if row[j] == 1:
            ci = i + 1
            cj = j + 1

moves_row = abs(3 - ci)
moves_col = abs(3 - cj)
print(moves_row + moves_col)
```[cite: 16]

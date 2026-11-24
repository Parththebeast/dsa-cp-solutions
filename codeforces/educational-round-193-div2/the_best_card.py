t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    num = []
    for j in range(n):
        num.append(j + 2)

    valid = True
    for k in range(n):
        if num[n - 1] % num[k] == 0 and k != n - 1:
            valid = False

    if not valid:
        print("NO")
    else:
        print("YES")
```[cite: 13]

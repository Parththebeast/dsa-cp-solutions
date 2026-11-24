t = int(input().strip())

for _ in range(t):
    ned = 0
    mj = 0
    l, r = map(int, input().split())

    for j in range(l, r + 1):
        if j % 2 == 0:
            ned += 1
        else:
            mj += 1

    if ned > mj:
        print("Ned")
    elif mj > ned:
        print("MJ")
    else:
        print("Draw")
```[cite: 15]

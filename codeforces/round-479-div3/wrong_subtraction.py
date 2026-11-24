n, k = map(int, input().split())

for _ in range(k):
    last_digit = n % 10
    if last_digit == 0:
        n = n // 10
    else:
        n = n - 1

print(n)
```[cite: 14]

n, k = map(int, input().split())
scores = list(map(int, input().split()))

count = 0
cutoff = scores[k - 1]

for score in scores:
    if score >= cutoff and score > 0:
        count += 1

print(count)
```[cite: 15]

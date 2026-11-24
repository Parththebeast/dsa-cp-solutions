n = int(input().strip())
count = 0

for _ in range(n):
    op = input().strip()
    if op == "++X" or op == "X++":
        count += 1
    elif op == "--X" or op == "X--":
        count -= 1

print(count)

t = int(input().strip())

for _ in range(t):
    a, b, c = map(int, input().split())
    nums = sorted([a, b, c])
    a = nums[0]
    b = nums[1]
    c = nums[2]
    rounds = min(b - a, c - b)
    print(rounds)

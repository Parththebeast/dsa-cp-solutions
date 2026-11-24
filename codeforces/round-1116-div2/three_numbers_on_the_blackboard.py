t = int(input().strip())

for _ in range(t):
    a, b, c = map(int, input().split())
    nums = sorted([a, b, c])
    ans = min(nums[2] - nums[0], nums[1])
    print(ans)


ans1 = 0

with open('2025/inputs/day3.txt') as file:
    for line in file:
        nums = list(map(int, line.strip()))
        mx = max(nums)
        if nums.index(mx) != len(nums) - 1:
            ans1 += mx*10 + max(nums[nums.index(mx)+1:])
        else:
            ans1 += mx + max(nums[:nums.index(mx)])*10
            
print(ans1)
        

ans2 = 0

def helper(nums, can_remove):
    if len(nums) == can_remove:
        return []
    mx = max(nums[:can_remove+1])
    idx = nums.index(mx)
    return [mx] + helper(nums[idx+1:], can_remove - idx)
    

with open('2025/inputs/day3.txt') as file:
    for line in file:
        nums = list(map(int, line.strip()))
        res = helper(nums, len(nums)-12)
        ans2 += int(''.join(map(str, res)))
        

print(ans2)
        
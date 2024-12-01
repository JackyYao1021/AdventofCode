from collections import defaultdict

left_dict = defaultdict(int)
right_dict = defaultdict(int)

with open("inputs/day1.txt", 'r') as file:
    for line in file:
        left, right = map(int, line.strip().split())
        left_dict[left] += 1
        right_dict[right] += 1

sum_similarity = 0

for left in left_dict.keys():
    num_left = left_dict[left]
    num_right = right_dict[left]
    sum_similarity += num_left*left*num_right


print(sum_similarity)


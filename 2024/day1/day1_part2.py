from collections import defaultdict

left_dic = defaultdict(int)
right_dic = defaultdict(int)

with open("inputs/day1.txt", 'r') as file:
    for line in file:
        left, right = map(int, line.strip().split())
        left_dic[left] += 1
        right_dic[right] += 1

sum_similarity = 0

for left in left_dic.keys():
    num_left = left_dic[left]
    num_right = right_dic[left]
    sum_similarity += num_left*left*num_right


print(sum_similarity)


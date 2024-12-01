import heapq

heap_left = []
heap_right = []

with open("inputs/day1.txt", 'r') as file:
    for line in file:
        left, right = map(int, line.strip().split())
        heapq.heappush(heap_left, left)
        heapq.heappush(heap_right, right)

sum = 0
length = len(heap_left)

for i in range(length):
    left = heapq.heappop(heap_left)
    right = heapq.heappop(heap_right)
    sum += abs(left - right)
print(sum)

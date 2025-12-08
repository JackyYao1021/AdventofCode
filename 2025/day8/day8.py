from heapq import heappop, heappush
from math import sqrt
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        
    def find(self, a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def union(self, a, b):
        rootA = self.find(a)
        rootB = self.find(b)

        if rootA == rootB:
            return
        if self.size[rootA] < self.size[rootB]:
            rootA, rootB = rootB, rootA
        self.parent[rootB] = rootA
        self.size[rootA] += self.size[rootB]
        
def cal_dis(p1, p2):
    return int(sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2))
                
               
n = 1000
with open("2025/inputs/day8.txt") as file:
    points = [tuple(map(int, line.strip().split(","))) for line in file]
    
dsu = DSU(len(points))
heap = []

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        heappush(heap, (cal_dis(points[i], points[j]), i, j))
        
while n > 0:
    dis, i, j = heappop(heap)
    if dsu.find(i) != dsu.find(j):
        dsu.union(i, j)
    n -= 1

dsu_count = []
for i in range(len(points)):
    if i == dsu.find(i):
        heappush(dsu_count, -dsu.size[i])

print(-heappop(dsu_count) * -heappop(dsu_count) * -heappop(dsu_count))

        
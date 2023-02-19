import sys
import math
sys.setrecursionlimit(50000)
input = sys.stdin.readline

n, m = map(int, input().split()) # 우주신, 신들과의 통로 개수
parent = [0] * (n + 1)

for i in range(1, n + 1):
	parent[i] = i

posistion_lst = [[None]]
for _ in range(n):
	a, b = map(int, input().split())
	posistion_lst.append((a, b))

edges_lst = []
for i in range(1, n + 1):
	for j in range(i + 1, n + 1):
		col = (posistion_lst[i][0] - posistion_lst[j][0]) ** 2
		row = (posistion_lst[i][1] - posistion_lst[j][1]) ** 2
		cost = math.sqrt(col + row)
		edges_lst.append((cost, i, j))
# print(edges_lst)

edges_lst2 = []
for _ in range(m):
	a, b = map(int, input().split())
	edges_lst2.append((a, b))

def find_parent(parent, x):
	if x != parent[x]:
		parent[x] = find_parent(parent, parent[x])
	return parent[x]

def union_parent(parent, a, b):
	a = find_parent(parent, a)
	b = find_parent(parent, b)
	if a < b:
		parent[b] = a
	else:
		parent[a] = b

for edge2 in edges_lst2: # 두 노드가 우선 연결된 경우 유니온 해준다.
	a, b = edge2 
	for edge in edges_lst:
		cost, a2, b2 = edge
		if ((a, b) == (a2, b2)) or ((a, b) == (b2, a2)):
			union_parent(parent, a, b)

edges_lst.sort()

result = 0
for edge in edges_lst:
	cost, a, b = edge
	if find_parent(parent, a) != find_parent(parent, b):
		union_parent(parent, a, b)
		result += cost
print("{:.2f}".format(result))
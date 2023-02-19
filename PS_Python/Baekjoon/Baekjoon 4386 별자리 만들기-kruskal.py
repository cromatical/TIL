import sys
import math
sys.setrecursionlimit(50000)
input = sys.stdin.readline

n = int(input()) # 별의 개수
parent = [0] * (n + 1)

for i in range(1, n + 1):
	parent[i] = i

star_position = [[None]] # 별들의 위치를 받기 위한 테이블
for _ in range(n):
	a, b = map(float, input().split()) # 별자리 위치
	star_position.append((a, b))

edges_lst = [] # 두 점의 별과 거리를 저장할 테이블
for i in range(1, n + 1): # 행
	for j in range(i + 1, n + 1): # 열, 피타고라스를 이용하여 두별사이의 거리를 구함
		col = (star_position[i][0] - star_position[j][0]) ** 2
		row = (star_position[i][1] - star_position[j][1]) ** 2
		cost = round(math.sqrt(col + row), 2) # round(x, n)을 통해 소수점 n번째 까지의 수를 구함
		edges_lst.append((cost, i, j)) # 테이블에 추가

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

edges_lst.sort()
# print(edges_lst)

result = 0 
for edge in edges_lst:
	cost, a, b = edge
	if find_parent(parent, a) != find_parent(parent, b):
		union_parent(parent, a, b)
		result += cost
print(result)
import sys
sys.setrecursionlimit(50000)
input = sys.stdin.readline

n, m = map(int, input().split()) # 점, 진행 차례 수
parent = [0] * (n + 1)

for i in range(1, n + 1):
	parent[i] = i

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

for i in range(m):
	a, b = map(int, input().split()) # 두점 입력
	if find_parent(parent, a) != find_parent(parent, b):
		union_parent(parent, a, b)
	else:
		break
if i != m - 1: # 사이클 없이 무사히 마무리 되면 0 출력
	print(i + 1) 
else:
	print(0)
	
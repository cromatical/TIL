import sys
sys.setrecursionlimit(50000)
input = sys.stdin.readline

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

n, m = map(int, input().split()) # 노드와 간선 입력
parent = [0] * (n + 1)

for i in range(1, n + 1):
	parent[i] = i

edges_lst = []
for _ in range(m):
	a, b, c = map(int, input().split())
	edges_lst.append((c, a, b))

edges_lst.sort() # 오름차순 정렬
result = 0 # 최소 신장트리의 길이 저장을 위한 변수
for edge in edges_lst:
	cost, a, b = edge
	if find_parent(parent, a) != find_parent(parent, b):
		union_parent(parent, a, b)
		result += cost

print(result)
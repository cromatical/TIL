import sys
input = sys.stdin.readline

v , e = map(int, input().split()) # 집, 도로 개수 입력
graph = [[] for _ in range(v + 1)] # 노드사이의 경로 저장 테이블
parent = [0] * (v + 1)
edges = [] # 간선을 넣는 테이블

for _ in range(e):
	a, b, c = map(int, input().split()) # a, b, c거리
	edges.append((c, a, b))

for i in range(1, v + 1):
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

edges.sort() # 간선의 길이가 가장 짧은 대로 정렬
result = 0 # 최소 길이를 저장하기 위해
max_value = 0 # 가장 큰 간선의 길이를 파악하기위해 

for edge in edges: # 간선을 하나씩 확인
	cost, a, b = edge
	if find_parent(parent, a) != find_parent(parent, b):
		union_parent(parent, a, b)
		result += cost
		if max_value < cost:
			max_value = cost

print(result - max_value)
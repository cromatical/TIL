def find_parent(parent, x):
	if parent[x] != x:
		parent[x] = find_parent(parent, parent[x])
	return parent[x]

def union_parent(parent, a, b):
	a = find_parent(parent, a)
	b = find_parent(parent, b)
	if a < b:
		parent[b] = a
	else:
		parent[a] = b

v, e = map(int, input().split()) # 노드와 간선의 개수
parent = [0] * (v + 1) # 부모테이블 초기화

edges = [] # 모든 간선을 담을 리스트 
result = 0 # 최종 비용을 담을 변수

for i in range(1, v + 1): # 부모테이블에서 자기 자신을 초기화
	parent[i] = i

for _ in range(e):
	a, b, cost = map(int, input().split()) # 간선의 정보입력
	edges.append((cost, a, b)) # 비용순으로 정렬하기 위해 첫번째원소를 비용으로 설정

edges.sort() # cost를 기준을 오름차순 정렬

for edge in edges: # 간선을 하나씩 확인
	cost, a, b = edge
	if find_parent(parent, a) != find_parent(parent, b): # 사이클이 발생하지 않은 경우에만 집합에 포함
		union_parent(parent, a, b)
		result += cost

print(result)

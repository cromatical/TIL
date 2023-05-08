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

v, e = map(int, input().split()) # 노드와 간선 개수입력
parent = [0] * (v + 1)

for i in range(1, v + 1):
	parent[i] = i

cycle = False # 사이클 여부 초기화

for i in range(e):
	a, b = map(int, input().split()) # 간선입력
	if find_parent(parent, a) == find_parent(parent, b): # 사이클 발생시
		cycle = True
		break
	else: # 사이클이 발생하지 않았다면 유니온실행
		union_parent(parent, a, b)

if cycle:
	print("사이클이 발생했습니다.")
else:
	print("사이클이 발생하지 않았습니다.")
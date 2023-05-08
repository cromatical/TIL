def find_parent(parent, x): # 특정원소가 속한 집합을 찾기
	if parent[x] != x: # 루트노드가 아니면 루트노드를 찾을 때까지 재귀적으로 호출.
		return find_parent(parent, parent[x])
	return x

def find_parent2(parent, x): # 기존 find_parent를 개선시킨 find_parent
	if parent[x] != x: # 루트노드가 아니면 루트노드를 찾을 때까지 재귀적으로 호출.
		parent[x] = find_parent2(parent, parent[x])
	return parent[x]

def union_parent(parent, a, b): # 두 원소가 속한 집합을 합치기
	a = find_parent(parent, a)
	b = find_parent(parent, b)
	if a < b:
		parent[b] = a
	else:
		parent[a] = b

v, e = map(int, input().split()) # 노드의 개수와 간선의 개수 입력받기
parent = [0] * (v + 1) # 부모테이블 초기화

for i in range(1, v + 1): # 부모 테이블상에서, 부모를 자기 자신으로 초기화
	parent[i] = i

# union 연산수행
for i in range(e):
	a, b = map(int, input().split())
	union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
print("각 원소가 속한 집합 :", end="")
for i in range(1, v + 1):
	print(find_parent(parent, i), end=" ")
print()

# 부모테이블 내용 출력
print("부모 테이블 :", end="")
for i in range(1, v + 1):
	print(parent[i], end=" ")




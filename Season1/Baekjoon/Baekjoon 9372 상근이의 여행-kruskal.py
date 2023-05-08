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

t = int(input()) # 테스트케이스 수

for _ in range(t):
	n, m = map(int, input().split()) # 국가의 수, 비행기의 종류
	parent = [0] * (n + 1)

	for i in range(1, n + 1):
		parent[i] = i

	result = [] # 최소신장트리 결과를 저장할 테이블
	edges_lst = [] # 입력받은 간선 저장할 테이블, cost비용으로 정렬
	for _ in range(m):
		a, b = map(int, input().split()) # 두점 a와 b를 입력
		edges_lst.append((a, b))
	
	for edge in edges_lst: 
		a, b = edge 
		if find_parent(parent, a) != find_parent(parent, b):
			union_parent(parent, a, b)
			result += [(a, b)]
	print(len(result)) # 길이 확인
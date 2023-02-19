import sys
sys.setrecursionlimit(50000)
input = sys.stdin.readline

n = int(input()) # 도시의 수
m = int(input()) # 여행계획에 속한 도시들의 수
parent = [0] * (n + 1) # 부모테이블 초기화

for i in range(1, n + 1): # 부모 테이블상에서, 부모를 자기 자신으로 초기화
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

for i in range(1, n + 1):
	visited_lst = list(map(int, input().split()))
	for j in range(1, len(visited_lst) + 1): # 
		if visited_lst[j - 1] == 1: # i번째 해당도시와 j는 연결되어있다.
			union_parent(parent, i, j) # union연산 실행

travel_lst = list(map(int, input().split())) # 여행계획에 속한 도시
print(parent)

parent_check = set([parent[i] for i in travel_lst])
print(parent_check)
if len(parent_check) == 1:
	print("YES")
else:
	print("NO")
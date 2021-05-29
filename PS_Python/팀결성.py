import sys
sys.setrecursionlimit(50000) # 재귀 제한 풀어주기
input = sys.stdin.readline 

n, m = map(int, input().split()) # 학생수, 팀을 합칠지, 같은팀인지 수행하는 연산수
parent = [0] * (n + 1) # 부모노드 확인을 위한 테이블 생성

for i in range(1, n + 1): # 부모노드 테이블 자기 자신노드로 초기화
	parent[i] = i

def find_parent(parent, x): # 부모노드 확인
	if x != parent[x]:
		parent[x] = find_parent(parent, parent[x])
	return parent[x]

def union_parent(parent, a, b): # 유니온 함수
	a = find_parent(parent, a)
	b = find_parent(parent, b)
	if a < b:
		parent[b] = a
	else:
		parent[a] = b

for _ in range(m): # 연산수행
	i, a, b = map(int, input().split()) # 연산종류, 노드 a, b입력
	if i == 0:
		union_parent(parent, a, b) # 팀합치기
	else:
		if find_parent(parent, a) == find_parent(parent, b): # 팀이 같은 경우
			print("YES")
		else: # 팀이 다른경우
			print("NO")

print(parent) # 팀 확인!
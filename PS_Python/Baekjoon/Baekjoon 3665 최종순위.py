import sys
from collections import deque
input = sys.stdin.readline

t = int(input()) # 테스트케이스 수

def topology_sort(n):
	result = []
	q = deque()

	for i in range(1, n + 1): # 처음 진입차수가 0인 노드 찾기
		if indegree[i] == 0:
			q.append(i)
	while q:
		if len(q) > 1: # 순위가 불확실한 경우 진입차수가 0 인개 여러개일 때
			print('?')
			return 
		now = q.popleft() # 현재 진입차수가 0인 노트
		result.append(now) # 위상정렬 테이블 넣기

		for i in graph[now]:
			indegree[i] -= 1
			if indegree[i] == 0: # 새로운 진입차수가 0 인경우 q에 넣어준다.
				q.append(i)
	if len(result) != n:
		print("IMPOSSIBLE")
		return 
	
	for i in result:
		print(i, end=' ')
	return 

for _ in range(t):
	n = int(input()) # 팀 수
	rank_lst = list(map(int, input().split())) # 작년 순위
	
	graph = [[] for _ in range(n + 1)]
	
	idx = 1
	for i in rank_lst[:-1]:
		graph[i] = rank_lst[idx:]
		idx += 1
	# print(graph)

	indegree = [0] * (n + 1)
	for i in range(1, n + 1):
		indegree[i] = n - 1 - len(graph[i])
	# print(indegree)
	m = int(input()) # 상대적 등수가 바뀐 개수
	
	for _ in range(m):
		a, b = map(int, input().split()) # 등수가 바뀐팀
		if rank_lst.index(a) > rank_lst.index(b): # 역방향
			graph[a].append(b)
			graph[b].remove(a)
			indegree[a] -= 1
			indegree[b] += 1 
		else: # 순차적일 떄
			graph[b].append(a)
			graph[a].remove(b)
			indegree[a] += 1
			indegree[b] -= 1 

	# print(graph)
	# print(indegree)
	topology_sort(n)
from collections import deque

v , e = map(int, input().split()) # 노드와 간선 개수 입력
indegree = [0] * (v + 1) # 모든 노드에 대한 진입차수 0 으로 초기화
graph = [[] for i in range(v + 1)] # 각 노드에 연결된 간선정보를 입력받기 위한 그래프

for _ in range(e):
	a, b = map(int, input().split()) # 노드a, b 정보 입력
	graph[a].append(b) # 노드 a -> b
	indegree[b] += 1 # 진입차수 1 증가

def topology_sort(): # 위상정렬 함수
	result = [] # 위상정렬 결과를 담을 테이블
	q = deque()

	for i in range(1, v + 1): # 처음 시작할 때 진입차수가 0인 노드를 큐에 삽입
		if indegree[i] == 0:
			q.append(i)
	
	while q: # q가 빌 때까지 수행. 만약 모든노드를 돌지 않았는데 q가 비어버리면 사이클이 존재하는 경우이다.
		now = q.popleft()
		result.append(now)

		for i in graph[now]: # 현재 노드와 연결된 노드들 진입차수 -1
			indegree[i] -= 1
			if indegree[i] == 0: # 새롭게 진입차수가 0이된 노드를 q에 추가
				q.append(i)

	for i in result: # 위상정렬 결과 출력
		print(i, end=' ')

topology_sort()

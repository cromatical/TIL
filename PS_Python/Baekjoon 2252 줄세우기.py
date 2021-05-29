import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split()) # 학생번호와, 두 학생 비교관계 
indegree = [0] * (n + 1) # 진입차수를 나타낼 테이블
graph = [[] for _ in range(n + 1)] # 두 학생의 관계를 나타낼 그래프 테이블

for _ in range(m):
	a, b = map(int, input().split()) # 학생 a, b입력
	graph[a].append(b)
	indegree[b] += 1

# print(graph)

def topology_sort():
	result = [] # 결과 저장 테이블
	q = deque()

	for i in range(1, n + 1): # 진입차수가 0인 초기노드 큐에 집어넣기
		if indegree[i] == 0:
			q.append(i)
	
	while q:
		now = q.popleft()
		result.append(now)
		# print(now)
		for i in graph[now]: # 현재 노드와 연결된 노드 찾기
			indegree[i] -= 1
			if indegree[i] == 0:
				q.append(i)
	
	for i in result:
		print(i, end=" ")

topology_sort()
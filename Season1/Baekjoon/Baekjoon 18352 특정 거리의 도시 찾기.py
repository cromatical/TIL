import sys
from collections import deque
input = sys.stdin.readline

n, m, k, x = map(int, input().split()) # 도시의 개수, 도로의 개수, 거리정보, 출발 도시번호

graph = [[] for i in range(n + 1)] # 그래프의 노드연결정보 저장할 테이블
node_distance = [0] * (n + 1) # 각 노드들의 거리를 저장할 테이블
visited = [False] * (n + 1) # 노드를 방문했는지 확인하는 테이블

for _ in range(m): 
	a, b = map(int, input().split())
	graph[a].append(b)
# print(graph)

def bfs(graph, start): # bfs 시작
	q = deque([start])
	node_distance[start] = 0
	visited[start] = True

	while q: # 더이상 갈곳이 없을 때까지
		now = q.popleft()
		previous = node_distance[now] # 현재의 거리를 저장

		for i in graph[now]: # 현재 노드로부터 갈수있는 노드들 탐색
			if visited[i] == False: # 방문안했으면 방문한다!
				visited[i] = True	
				q.append(i)
				node_distance[i] = previous + 1

bfs(graph, x)
# print(node_distance)

cnt = 0
for i in range(1, n + 1):
	if node_distance[i] == k: # 시작노드로부터 i번째 노드의 최단거리가 k와 동일한 경우 
		cnt += 1
		print(i)
if cnt == 0:
	print(-1)
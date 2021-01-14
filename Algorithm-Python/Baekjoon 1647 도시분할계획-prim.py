import sys
input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split()) # 마을과 도로 입력

distance = [INF] * (v + 1) # 신장트리가 형성될때 필요한 가장 작은 간선을 저장할 테이블
visited = [False] * (v + 1) # 방문확인 테이블
graph = [[INF] * (v + 1) for _ in range(v + 1)]

for a in range(1, v + 1): # 자기자신 0으로 초기화
	for b in range(1, v + 1):
		if a == b:
			graph[a][b] == 0

for _ in range(e): # 입력
	a, b, c = map(int, input().split())
	graph[a][b] = c
	graph[b][a] = c

def get_smallest():
	min_value = INF
	idx = 0
	for i in range(1, v + 1): # 그중 거리가 가장 작은 노드 선택
		if  distance[i] < min_value and not visited[i]:
			min_value = distance[i]
			idx = i
	return idx

def prim(start):
	for i in range(v + 1): # 방문과 distance초기화
		visited[i] = False
		distance[i] = INF

	distance[start] = 0
		
	for _ in range(1, v + 1): # 노드의 개수 만큼 돈다.
		now = get_smallest()
		visited[now] = True
		for next_node in range(1, v + 1): # 다음노드 확인
			if graph[now][next_node] != INF:
				if not visited[next_node] and graph[now][next_node] < distance[next_node]:
					distance[next_node] = graph[now][next_node]

start = 1
prim(start)
print(sum(distance[1:]) - max(distance[1:]))
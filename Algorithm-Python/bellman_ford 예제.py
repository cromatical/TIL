INF = int(1e9) # 무한을 의미하는 10억으로 세팅

n, e = map(int, input().split()) # 노드의 개수와 간선
start = int(input()) # 시작노드
graph = [[] for i in range(n + 1)] # 각 노드에 연결되어 있는 정보를 넣기 위한 리스트
distance = [INF] * (n + 1) # 각 거리 초기화

for _ in range(e): # 각 노드에 연결되어있는 노드와 간선의 길이
	a, b, c = map(int, input().split())
	graph[a].append((b, c))
print(graph)

def bellman_ford(start):
	distance[start] = 0
	for _ in range(n - 1): # 노드 개수 -1 만큼 반복
		for now in range(1, n + 1): # 현재의 노드 확인
			for i in graph[now]: # 각 정점마다 모든 인접 정점들을 탐색
				if distance[i[0]] > distance[now] + i[1]: # 기존 인접 정점까지의 거리 > 기존 현재 정점까지의 거리 + 현재 정접부터 인접 정점까지 거리
					distance[i[0]] = distance[now] + i[1]

	for now in range(1, n + 1): # 음수 사이클 존재하는지 확인 (n - 1)번 돌고도 갱신할 거리 값이 존재한다면 음수 사이클 존재
		for i in graph[now]:
			if distance[i[0]] > distance[now] + i[1]:
				return 0
	return 1

result = bellman_ford(start)
if result == 1: # 음수 사이클이 아닌경우
	for i in range(1, n + 1):
		if distance[i] == INF:
			print("INF")
		else:
			print(distance[i], end=" ")
else: # 음수 사이클인 경우
	print("negative cycle")

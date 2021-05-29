import sys
input = sys.stdin.readline
INF = int(1e9)

n, e = map(int, input().split()) # 버스, 노선의 개수
graph = [[] for _ in range(n + 1)] # 각 노드들에 대한 정보 저장 테이블
distance = [INF] * (n + 1)

for _ in range(e):
	a, b, c = map(int, input().split()) # 버스, 노선, 거리
	graph[a].append((b, c))

def bellman_ford(start): # 벨만포드 알고리즘
	distance[start] = 0

	for _ in range(n - 1):
		for now in range(1, n + 1):
			if distance[now] != INF: # INF에서 값이 줄어드는걸 방지하기 위해
				for i in graph[now]:
					cost = distance[now] + i[1]
					if cost < distance[i[0]]:
						distance[i[0]] = cost

	for now in range(1, n + 1): # 음의 사이클이 존재하는지 확인
		if distance[now] != INF: # 시작부분에서 각 노드들간 거리 확인을 위해 만약 INF부분이 있으면 도달할수 없는 경우다.
			for i in graph[now]:
				cost = distance[now] + i[1]
				if cost < distance[i[0]]:
					return -1
	return 1

start = 1
result = bellman_ford(start) # 결과

if result == -1:
	print(-1)
else:
	for i in range(2, n + 1):
		if distance[i] < INF:
			print(distance[i])
		else:
			print(-1)

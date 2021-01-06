INF = int(1e9) # 무한을 의미하는 값으로 10억 세팅

n = int(input()) # 노드의 개수
e = int(input()) # 간선의 개수

graph = [[INF] * (n + 1) for _ in range(n + 1)] # 2차원 리스트를 만들고, 모든 값을 무한으로 초기화

for a in range(1, n + 1): # 자기 자신에서 자기 자신으로 가는 거리는 0으로 초기화
	for b in range(1, n + 1):
		if a == b:
			graph[a][b] = 0

for _ in range(e): # 각 간선에 대한 정보를 입력 받아서 그 값으로 초기화
	a, b, c = map(int, input().split()) # 출발, 도착, 거리
	graph[a][b] = c

for k in range(1, n + 1): # 점화식에 따라 플로이드 워셜 알고리즘 수행
	for a in range(1, n + 1):
		for b in range(1, n + 1):
			graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n + 1): # 수행결과 출력
	for b in range(1, n + 1):
		if graph[a][b] == INF:
			print("INF")
		else:
			print(graph[a][b], end=" ")
	print()

	

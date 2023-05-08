import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
	a, b, c = map(int, input().split())
	if graph[a][b] == INF: # 해당 노드들 사이의 거리가 업데이트가 안된경우 업뎃해줌
		graph[a][b] = c
	else: # 해당 노드들 사이의 길이 하나가 아닌경우가 있으므로! 하지만 최단경로를 묻기 때문에 새로운 거리가 기존값보다 작으면 업뎃해줌
		if graph[a][b] > c:
			graph[a][b] = c

for a in range(1, n + 1): # 자기자신으로 가는 거리는 0으로 초기화
	for b in range(1, n + 1):
		if a == b:
			graph[a][b] = 0

for k in range(1, n +1):
	for a in range(1, n + 1):
		for b in range(1, n + 1):
			graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


for a in range(1, n + 1):
	for b in range(1, n + 1):
		if graph[a][b] == INF:
			print(0, end=" ") # 갈수없는 경우 0 으로 출력
		else:
			print(graph[a][b], end=" ")
	print("")
	
		
	


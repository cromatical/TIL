import sys
input = sys.stdin.readline
INF = int(1e9)

n, e = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(n):
	for b in range(n):
		if a == b:
			graph[a][b] = 0

for _ in range(e):
	a, b, c = map(int, input().split())
	graph[a][b] = c
	graph[b][a] = c

v1, v2 = map(int, input().split())

for k in range(1, n + 1):
	for a in range(1, n + 1):
		for b in range(1, n + 1):
			graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

distance1 = graph[1][v1] + graph[v1][v2] + graph[v2][n]
distance2 = graph[1][v2] + graph[v2][v1] + graph[v1][n]
distance = min(distance1, distance2)
if distance < INF:
	print(distance)
else:
	print(-1)
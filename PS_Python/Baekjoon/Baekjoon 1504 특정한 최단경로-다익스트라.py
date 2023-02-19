import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(e):
	a, b, c = map(int, input().split())
	graph[a].append((b, c))
	graph[b].append((a, c))

v1, v2 = map(int, input().split())

def dijkstra(start, end):
	distance = [INF] * (n + 1)

	q = []
	heapq.heappush(q, (0, start))
	distance[start] = 0
	
	while q:
		dist, now = heapq.heappop(q)
		if distance[now] < dist:
			continue
		else:
			for i in graph[now]:
				cost = dist + i[1]
				if cost < distance[i[0]]:
					distance[i[0]] = cost
					heapq.heappush(q, (cost, i[0]))
	return distance[end]

# 거리를 1 -> v1 -> v2 -> n과 1 -> v2 -> v1 -> n이 더 짧은지 비교
distance1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, n)
distance2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, n)
distance = min(distance1, distance2)
if distance < INF:
	print(distance)
else:
	print(-1)
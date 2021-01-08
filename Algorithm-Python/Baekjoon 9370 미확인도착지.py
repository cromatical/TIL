import heapq
import sys
input = sys.stdin.readline
INF = (1e9)

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

T = int(input()) # 테스트케이스 개수 입력
for _ in range(T):
	n, m, t = map(int, input().split()) # 교차로, 도로, 목적지 개수
	s, g, h = map(int, input().split()) # 출발지, 교차로 g와h사이의 도로를 지나감
	
	graph = [[] for _ in range(n + 1)]
	
	for _ in range(m): # 간선의 개수만큼 입력
		a, b, d = map(int, input().split()) # a-b사이의 거리가d인 양방향 도로가 있다.
		graph[a].append((b, d))
		graph[b].append((a, d))
	
	goal_lst = [int(input()) for _ in range(t)] # 목적지 후보

	success = []
	for goal in goal_lst:
		result1 = dijkstra(s, g) + dijkstra(g, h) + dijkstra(h, goal) # s -> g -> h -> goal 최단경로를 확인할 때
		result2 = dijkstra(s, h) + dijkstra(h, g) + dijkstra(g, goal) # s -> h -> g -> goal 최단경로를 확인할 때
		result = min(result1, result2)
		if (result < INF and result == dijkstra(s, goal)): # 목적지까지 우회하지 않고 최단거리로 이동할꺼기 때문에 비교
			success.append(goal) 

	for goal in goal_lst:
		result1 = dijkstra(s, g) + dijkstra(g, h) + dijkstra(h, goal)
		if goal not in success:
			if (result < INF):
				

	success.sort() # 오름차순으로 정렬
	for val in success:
		print(val, end=' ')
	print()
	







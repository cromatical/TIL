import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, c = map(int, input().split()) # 도시의 개수, 통로의 개수, 시작 도시
graph = [[] for _ in range(n + 1)] # 각 노드의 정보테이블
distance = [INF] * (n + 1) # 최단경로

for _ in range(m): # 통로 개수 만큼
	x, y, z = map(int, input().split()) # x도시에서 y도시로 , 걸린시간 : z
	graph[x].append((y, z))

def dijkstra(start):
	q = [] # 우선순위를 위한 초기 테이블 생성
	heapq.heappush(q, (0, start))
	distance[start] = 0

	while q:
		dist, now = heapq.heappop(q)
		if distance[now] < dist: # 이미 방문했을 경우 최단경로를 가지고 있으므로 할 필요가 없다.
			continue
		else:
			for i in graph[now]: # 현재 노드에서 갈 수 있는 이웃노드들
				cost = dist + i[1]
				if cost < distance[i[0]]: # 기존 최단경로보다 작을 경우 업데이트
					distance[i[0]] = cost
					heapq.heappush(q, (cost, i[0])) # 우선순위 큐에 푸쉬

dijkstra(c) # 다익스트라 실행
# print(distance)

cnt_city = 0 # 현재 도시에서 보낼수 있는 도시 수
max_time = 0 # 도시들이 모두 메세지를 받는 데까지 걸리는 시간
for i in range(1, n + 1):
	if distance[i] == INF:
		continue
	else:
		if distance[i] != 0:
			cnt_city += 1
		if max_time < distance[i]: # 걸리는 최대시간 확인
			max_time = distance[i]
print("도시 수 :", cnt_city, "총 걸리는 시간 :", max_time)


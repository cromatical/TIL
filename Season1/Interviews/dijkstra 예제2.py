import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split()) # 노드와 간선의 개수 입력
start = int(input()) # start노드 지정
graph = [[] for _ in range(n + 1)] # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 생성
distance = [INF] * (n + 1) # 각 노드별 거리초기테이블 생성

for _ in range(m): # 노드에 대한 간선 정보 입력
	a, b, c = map(int, input().split())
	graph[a].append((b, c))

def dijkstra(start):
	q = []
	heapq.heappush(q, (0, start)) # 시작노드로 가기 위한 최단경로 0, 큐에 삽입
	distance[start] = 0

	while q: # 큐가 비어있지 않다면!!
		dist, now = heapq.heappop(q) # 가장 최단거리에 해당되는 노드와 거리 뽑기
		if distance[now] < dist: # 현재노드가 이미 처리된적 있는 노드라면 무시
			continue
		for i in graph[now]: # 현재 노드와 연결된 다른 인접한 노드들을 확인
			cost = dist + i[1]
			if cost < distance[i[0]]:
				distance[i[0]] = cost
				heapq.heappush(q, (cost, i[0])) # 우선순위 큐에 추가

dijkstra(start) # 다익스트라 알고리즘 수행.

for i in range(1, n + 1):
	if distance[i] < INF: # 도달할 수 있는 경우
		print(distance[i])
	else: # 만약 도달할 수 없는 경우 무한으로 출력
		print("INF")
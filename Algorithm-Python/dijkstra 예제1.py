import sys

input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억 설정

n, m = map(int, input().split()) # 노드의 개수, 간선의 개수 입력받기
start = int(input()) # 시작 노드 번호 입력
graph = [[] for i in range(n + 1)] # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
visited = [False] * (n + 1) # 방문한 적이 있는지 체크하는 목적의 리스트 생성
distance = [INF] * (n + 1) # 각 노드 최단거리 테이블 모두 무한으로 초기화

for _ in range(m): # 각 노드에 대한 정보 입력
	a, b, c = map(int, input().split()) # a -> b, c : 간선의 길이
	graph[a].append((b, c))


def get_smallest_node(): # 방문하지 않은 노드 중에서 가장 최단 거리가 짧은 노드의 번호를 반환
	min_value = INF
	index = 0 # 가장 최단 거리가 짧은 노드
	for i in range(1, n + 1):
		if distance[i] < min_value and not visited[i]:
			min_value = distance[i]
			index = i
	return index


def dijkstra(start):
	distance[start] = 0
	visited[start] = True

	for j in graph[start]:
		distance[j[0]] = j[1] # start노드에서 이웃노드들에 대한 거리
	
	for _ in range(n - 1): # 시작노드를 제외한 n - 1개의 노드에 대해 반복
		now = get_smallest_node() # 현재 최단거리가 가장 짧은 노드꺼내서 방문처리.
		visited[now] = True
		for j in graph[now]: # 현재 노드와 연결된 다른 노드 확인
			cost = distance[now] + j[1]
			if cost < distance[j[0]]: # 현재 노드와의 거리와 이전에 있던 거리와 비교
				distance[j[0]] = cost


dijkstra(start) # 다익스트라 알고리즘 실행

for i in range(1, n + 1):
	if distance[i] == INF: # 만약 도달할 수 없는 경우 무한으로 출력
		print("INF")
	else: # 도달할 수 있는 경우 
		print(distance[i])

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split()) # 노드와 간선의 개수
graph = [[INF] * (v + 1) for _ in range(v + 1)]
visited = [False] * (v + 1) # 방문 여부 리스트
distance = [INF] * (v + 1) # 거리 테이블

for a in range(1, v + 1): # 자기자신은 0 으로 초기화
	for b in range(1, v + 1):
		if a == b:
			graph[a][b] = 0

for _ in range(e):
	a, b, c = map(int, input().split())
	graph[a][b] = c
	graph[b][a] = c

def get_smallest():
	min_value = INF
	idx = 0
	for i in range(1, v + 1): # 그중 거리가 가장 작은 노드 선택
		if  distance[i] < min_value and not visited[i]:
			min_value = distance[i]
			idx = i
	return idx

def prim(start):
	for i in range(1, v + 1): # distance와 visited배열 초기화
		visited[i] = False
		distance[i] = INF
	
	distance[start] = 0
	for i in range(1, v + 1):
		now_node = get_smallest()
		visited[now_node] = True # 방문표시

		for next_node in range(1, v + 1):
			if graph[now_node][next_node] != INF: # 현재 노드와 이어진 노드들
				if not visited[next_node] and graph[now_node][next_node] < distance[next_node]: # 가장작은 거리로 업뎃
					distance[next_node] = graph[now_node][next_node]

start = 1
prim(start)
print(sum(distance[1:]))
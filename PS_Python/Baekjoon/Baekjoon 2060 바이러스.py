import sys
input = sys.stdin.readline

n = int(input()) # 컴퓨터의 수
m = int(input()) # 네트워크상 연결되어 있는 컴퓨터의 쌍

graph = [[] for _ in range(n + 1)]

for i in range(m):
	a, b = map(int, input().split())
	graph[b].append(a)
	graph[a].append(b)

visited = [False for _ in range(n + 1)]

def dfs(graph, v, visited): # dfs 탐색
	visited[v] = True

	for i in graph[v]:
		if visited[i] == False:
			dfs(graph, i, visited)

dfs(graph, 1, visited)
print(visited.count(1) - 1) # 처음에 감염된 컴퓨터를 제외하고 감염된 컴퓨터의 수 
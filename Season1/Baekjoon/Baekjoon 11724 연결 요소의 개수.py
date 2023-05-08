import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
	a, b = map(int, input().split())
	graph[b].append(a)
	graph[a].append(b)

def dfs(graph, v, visited):
	visited[v] = True

	for i in graph[v]:
		if visited[i] == False:
			dfs(graph, i, visited)

cnt = 0
for i in range(1, n + 1):
	if visited[i] == False:
		cnt += 1
		dfs(graph, i, visited)
print(cnt)
from collections import deque
import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for i in range(m):
	a, b = map(int, input().split())
	graph[b].append(a)
	graph[a].append(b)

def dfs(graph, v, visited):
	visited[v] = True
	print(v, end=" ")

	for i in graph[v]:
		if visited[i] == False:
			dfs(graph, i, visited)

def bfs(graph, v, visited):
	q = deque([v])
	visited[v] = True

	while (q):
		now = q.popleft()	
		print(now, end=" ")

		for i in graph[now]:
			if visited[i] == False:
				q.append(i)
				visited[i] = True

# print(graph)
new_graph = []
for i in graph:
	new = sorted(i)
	new_graph.append(new)
# print(new_graph)

visited = [False] * (n + 1)
dfs(new_graph, v, visited)
print("")

visited = [False] * (n + 1)
bfs(new_graph, v, visited)
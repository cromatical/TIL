# DFS함수 구현
def dfs(graph, v, visited):
	visited[v] = True # 현재노드 방문
	print(v, end=' ')
	
	for i in graph[v]: # 현재노드와 연결된 다른 노드를 재귀적으로 방문
		if not visited[i]:
			dfs(graph, i, visited)

# 각 노드가 연결된 정보를 리스트 자료형으로 표현
graph = [
	[],
	[2, 3, 8],
	[1, 7],
	[1, 4, 5],
	[3, 5],
	[3, 4],
	[7],
	[2, 6, 7],
	[1, 7]
]

# 각 노드가 방문한 정보를 리스트 자료형으로 표현
visited = [False] * 9

# dfs함수 호출
dfs(graph, 1, visited)
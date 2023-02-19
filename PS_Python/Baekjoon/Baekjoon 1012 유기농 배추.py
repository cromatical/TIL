import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(graph, i, j): # dfs 탐색
	if i < 0 or i >= n or j < 0 or j >= m:
		return 0
	if graph[i][j] == 1:
		graph[i][j] = 0
		dfs(graph, i, j - 1) # 좌 
		dfs(graph, i, j + 1) # 우  
		dfs(graph, i - 1, j) # 상 
		dfs(graph, i + 1, j) # 하
		return 1
	return 0

for i in range(int(input())):
	m, n, k = map(int, input().split()) # 가로, 세로, 배추개수

	graph = [[0 for _ in range(m)] for _ in range(n)]
	
	for _ in range(k):
		a, b = map(int, input().split())
		graph[b][a] = 1

	# for i in graph: # 맵 확인
	# 	print(i)

	cnt = 0
	for i in range(n):
		for j in range(m):
			if graph[i][j] == 1:
				cnt += dfs(graph, i, j)
	print(cnt)
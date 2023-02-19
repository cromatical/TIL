import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

graph = []
for _ in range(n):
	graph.append(list(map(int, input().split())))

s, x, y = map(int, input().split())

move_lst = [[0, -1], [-1, 0], [0, 1], [1, 0]] # 왼, 위, 오, 아

def bfs(graph):
	q = deque()
	for num in range(1, k + 1):
		for i in range(n):
			for j in range(n):
				if graph[i][j] == num:
					q.append((i, j))
					break
	time = 0
	while q:
		now = q.popleft()
		r1, c1 = now
		for move in move_lst:
			r2, c2 = move
			if r1 + r2 >= 0 and r1 + r2 < n and c1 + c2 >= 0 and c1 + c2 < n:
				for i in range(1, k + 1):
					if graph[r1][c1] == i and graph[r1 + r2][c1 + c2] == 0:
						graph[r1 + r2][c1 + c2] = i
						q.append((r1 + r2, c1 + c2))
						break
		
		a, b = q[0]
		if graph[r1][c1] == 3 and graph[a][b] == 1:
			time += 1
		if time == s:
			break

bfs(graph)
# for i in graph:
# 	print(i)
# print("")
print(graph[x - 1][y - 1])

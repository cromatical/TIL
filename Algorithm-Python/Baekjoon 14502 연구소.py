import sys
from collections import deque
from itertools import combinations
import copy
input = sys.stdin.readline

n, m = map(int, input().split()) # 행렬 사이즈

graph = []
for _ in range(n):
	graph.append(list(map(int, input().split())))

for i in graph:
	print(i)
print("")

move_lst = [[-1, 0], [0, 1], [1, 0], [0, -1]] # 위, 오른쪽, 아래, 왼쪽

def bfs(graph, n, m):
	q = deque()
	q1 = deque()
	for i in range(n):
		for j in range(m):
			if graph[i][j] == 2:
				q.append((i, j))
			elif graph[i][j] == 0:
				q1.append((i, j))
	# print(q)
	wall_lst = list(combinations(q1, 3))
	
	safe_space = []

	for three_wall in wall_lst:
		new_q = copy.deepcopy(q)
		new_graph = copy.deepcopy(graph)
		
		for wall in three_wall:
			r, c = wall
			new_graph[r][c] = 1
		
		while new_q:
			now = new_q.popleft()
			r1, c1 = now 
			for move in move_lst:
				r2, c2 = move
				if (r1 + r2 >= 0 and r1 + r2 < n and c1 + c2 >= 0 and c1 + c2 < m):
					if new_graph[r1 + r2][c1 + c2] == 0:
						new_graph[r1 + r2][c1 + c2] = 2
						new_q.append((r1 + r2, c1 + c2))
		cnt = 0
		for i in range(n):
			for j in range(m):
				if new_graph[i][j] == 0:
					 cnt += 1

		if cnt not in safe_space:
			safe_space.append(cnt)
	return sorted(safe_space, reverse=True)[0]

result = bfs(graph, n, m)
print(result)

# for i in graph:
# 	print(i)
# print("")

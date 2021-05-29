import sys
from collections import deque
input = sys.stdin.readline

n, l, r = map(int, input().split()) # 행렬 사이즈, 두 나라사이의 인구 차이가 l <= r 사이

graph = []
for _ in range(n):
	graph.append(list(map(int, input().split())))
for i in graph:
	print(i)
print("")

visit = []
for _ in range(n):
	visit.append([False] * n)
for i in visit:
	print(i)
print("")

go_lst = [[0, -1], [-1, 0], [0, 1], [1, 0]] # 왼, 위, 오, 아
cnt = 0 

for i in range(n):
	for j in range(n):
		if visit[i][j] == False:
			idx_lst = []
			idx_lst.append((i, j))

			q = deque()
			q.append((i, j))
			
			visit[i][j] = True
			while q:
				now = q.popleft()
				for go in go_lst:
					if now[0] + go[0] >=0 and now[0] + go[0] < n and now[1] + go[1] >=0 and now[1] + go[1] < n:
						if visit[now[0] + go[0]][now[1] + go[1]] == False and l <= abs(graph[now[0]][now[1]] - graph[now[0] + go[0]][now[1] + go[1]]) and abs(graph[now[0]][now[1]] - graph[now[0] + go[0]][now[1] + go[1]]) <= r:
							idx_lst.append((now[0] + go[0], now[1] + go[1]))
							q.append((now[0] + go[0], now[1] + go[1]))
							visit[now[0] + go[0]][now[1] + go[1]] = True
			
			result = 0
			for k in idx_lst:
				result += graph[k[0]][k[1]]
			result = result // len(idx_lst)
			for k in idx_lst:
				graph[k[0]][k[1]] = result
			if len(idx_lst) >= 2:
				cnt += 1

for i in graph:
	print(i)
print("")

print(cnt)
		

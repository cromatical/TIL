import sys
import copy
from itertools import combinations
input = sys.stdin.readline

n = int(input())

graph = []
for _ in range(n):
	graph.append(list(input().split()))

t = []
s = []
x = []
for i in range(n):
	for j in range(n):
		if graph[i][j] == 'T':
			t.append((i, j))
		elif graph[i][j] == 'S':
			s.append((i, j))
		else:
			x.append((i, j))
# print(t)
new_x = list(combinations(x, 3))

def teacher_move(graph, i, j, d):
	direction = [(0, -1), (-1, 0), (0, 1), (1, 0)]
	i2, j2 = direction[d]

	if i + i2 >= n or j + j2 >= n or i + i2 < 0 or j + j2 < 0:
		return 0
	if d == 0:
		if graph[i + i2][j + j2] == 'S':
			return 1
		elif graph[i + i2][j + j2] == 'O':
			return 0
		else:
			return teacher_move(graph, i + i2, j + j2, d)
	if d == 1:
		if graph[i + i2][j + j2] == 'S':
			return 1
		elif graph[i + i2][j + j2] == 'O':
			return 0
		else:
			return teacher_move(graph, i + i2, j + j2, d)
	if d == 2:
		if graph[i + i2][j + j2] == 'S':
			return 1
		elif graph[i + i2][j + j2] == 'O':
			return 0
		else:
			return teacher_move(graph, i + i2, j + j2, d)
	if d == 3:
		if graph[i + i2][j + j2] == 'S':
			return 1
		elif graph[i + i2][j + j2] == 'O':
			return 0
		else:
			return teacher_move(graph, i + i2, j + j2, d)

def check_student(graph):
	for teacher in t:
		i, j = teacher
		for k in range(3): # 왼, 위, 오, 아
			result = teacher_move(graph, i, j, k)
			if result == 1:
				return 0
	return 1

def build_pillar():
	for pillars in new_x:
		new_graph = copy.deepcopy(graph)
		for pillar in pillars:
			i, j = pillar
			new_graph[i][j] = 'O'
		result = check_student(new_graph)
		if result == 1:
			return 1
	return 0
	
result = build_pillar()
if result == 1:
	print("YES")
else:
	print("NO")
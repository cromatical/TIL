import sys
import copy
from itertools import combinations
input = sys.stdin.readline

n = int(input()) # n x n 행렬 

graph = [] # 행렬 테이블 초기화
for _ in range(n):
	graph.append(list(input().split()))

t = [] # 선생님
s = [] # 학생
x = [] # 빈공간
for i in range(n):
	for j in range(n):
		if graph[i][j] == 'T':
			t.append((i, j))
		elif graph[i][j] == 'S':
			s.append((i, j))
		else:
			x.append((i, j))
# print(t)
new_x = list(combinations(x, 3)) # 기둥을 세울 3개의 좌표값

def teacher_move(new_graph, i, j, d): # (i, j)는 선생님의 좌표
	direction = [(0, -1), (-1, 0), (0, 1), (1, 0)] # 왼, 위, 오, 아
	i2, j2 = direction[d]

	if i + i2 >= n or j + j2 >= n or i + i2 < 0 or j + j2 < 0:
		return 0
	if new_graph[i + i2][j + j2] == 'S':
		return 1
	elif new_graph[i + i2][j + j2] == 'O':
		return 0
	else:
		return teacher_move(new_graph, i + i2, j + j2, d)

def check_student(new_graph):
	for teacher in t: 
		i, j = teacher
		for k in range(3): # 왼, 위, 오, 아
			result = teacher_move(new_graph, i, j, k)
			if result == 1: # 선생님이 학생을 지켜보는 경우
				return 0
	return 1

def build_pillar():
	for pillars in new_x: # 콤비네이션 함수를 통해서 3개의 빈공간을 기둥을 세워준다.
		new_graph = copy.deepcopy(graph) # 기존의 그래프는 영향을 주면 안되잖아
		for pillar in pillars: # 3개씩 묶은 하나의 경우를 가지고 기둥을 세워준다.
			i, j = pillar
			new_graph[i][j] = 'O'
		result = check_student(new_graph)
		if result == 1: # 기둥을 3개 세웠는데 선생님이 학생을 못찾을 경우 리턴
			for i in new_graph:
				print(i)
			print("")
			return 1
	for i in new_graph:
		print(i)
	print("")
	return 0 # 기둥으로 학생을 못가린경우
	
result = build_pillar()
if result == 1:
	print("YES")
else:
	print("NO")
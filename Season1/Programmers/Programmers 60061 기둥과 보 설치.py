import sys
from collections import deque
input = sys.stdin.readline

n = int(input()) # 2차원 배열 사이즈
n += 1
mat = [[0] * n for i in range(n)]
# for i in mat:
# 	print(i)
# print("")

# [x, y, a, b], 
# [x, y]는 기둥과 보의 교차점 좌표 
# a는 구조물의 종류를 나타냄 0:기둥, 1:보
# b는 구조물을 설치할지 삭제할지 1:설치, 0:삭제

build_frame = deque([[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]])
# build_frame = deque([[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]])

build = []
time = 1

while build_frame:
	x, y, a, b = build_frame.popleft()

	# print("time :", time, [x, y], a, b)
	time += 1

	if a == 1 and b == 1: # 보를 설치할 때
		# print(n - 1 - y, x)
		# print(n - y, x)
		# print(n - y, x + 1)
		if mat[n - y][x] > 0 or mat[n - y][x + 1] > 0 or (mat[n - 1 - y][x] == 2 and mat[n - 1 - y][x + 1] == 2):
			mat[n - 1 - y][x] += 2
			mat[n - 1 - y][x + 1] += 2
			build.append([x, y, a])
		
	elif a == 1 and b == 0: # 보를 삭제할 때
		if mat[n - 1 - y][x] >= 4 and mat[n - 1 - y][x + 1] >= 4:
			if (mat[n - 1 - y + 1][x - 1] == 1 and mat[n - 1 - y + 1][x + 1] == 1) or mat[n - 1 - y + 1][x] == 1:
				mat[n - 1 - y][x] -= 2
				mat[n - 1 - y][x + 1] -= 2
				build.remove([x, y, a])
		else:
			mat[n - 1 - y][x] -= 2
			mat[n - 1 - y][x + 1] -= 2
			build.remove([x, y, a])

	elif a == 0 and b == 1: # 기둥을 설치할 때
		# 기둥을 설치할 때 y측이 바닥이거나 밑에 보가있거나 기둥이 있어야한다.
		# print(n - 1 - y, x)
		if y == 0 or mat[n - 1 - y][x] == 2 or mat[n - y][x] == 1 or mat[n - y][x] == 3:
			mat[n - 1 - y][x] += 1
			build.append([x, y, a])

	else: # 기둥을 삭제할 때
		mat[n - 1 - y][x] -= 1
		build.remove([x, y, a])
	
	# for i in mat:
	# 	print(i)
	# print("")

build.sort()
# print(build)
# n x n 의 정사각형이 있다.
# 가장왼쪽 좌표는 (1, 1)이며, user가 있다.
# user는 상, 하, 좌, 우 방향으로 이동이 가능하며 1칸씩 이동한다.
# 입력으로 행동을 받아서 최종 좌표의 위치를 구하라.
# 정사각형을 벗어나는 움직임은 무시된다.

n = int(input())

action_lst = list(input().split()) # 행동 리스트

i, j = 1, 1 # user 스타트 위치
for action in action_lst:
	if (action == 'R'): # n x n 정사각형의 범위 체크
		if (j + 1) < n:
			j += 1
	elif (action == 'L'):
		if (J - 1) > 1:
			J -= 1
	elif (action == 'U'):
		if (i - 1) > 1:
			i -= 1
	else:
		if (i + 1) < n:
			i += 1

print(i, j)
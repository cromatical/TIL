import sys
input = sys.stdin.readline
from collections import deque

n = int(input()) # 보드의 크기
board = [[0] * n for i in range(n)]
# print(board)

k = int(input()) # k개의 사과
for _ in range(k):
	i, j = map(int, input().split()) # 사과의 위치
	board[i - 1][j - 1] = 1
# print(board)	

l = int(input()) # 뱀의 방향전환 횟수
l_lst = []
for _ in range(l):
	a, b = input().split()
	l_lst.append((int(a), b)) # (시간, 방향)

move_lst = [[-1, 0], [0, 1], [1, 0], [0, -1]] # 위, 오른쪽, 아래 ,왼쪽

snake = deque([[0, 0]]) # 뱀의 머리 부분
board[0][0] = 2
snake_move = 1

# for i in board:
# 	print(i)
# print("")

total_time = 0
game_over = 0
idx = 0

while 1:
	total_time += 1 
	head = [snake[-1][i] + move_lst[snake_move][i] for i in range(2)] # 뱀의 머리가 움직일 곳
	if head[0] < 0 or head[1] < 0 or head[0] >= n or head[1] >= n: # 맵을 벗어난 경우
		game_over = 1
		break
	if board[head[0]][head[1]] == 2: # 몸통을 만나는 경우
		game_over = 1
		break

	tail = snake.popleft()
	board[tail[0]][tail[1]] -= 2

	if board[head[0]][head[1]] == 1: # 사과가 있는 경우
		board[tail[0]][tail[1]] += 2
		snake.appendleft(tail) # 꼬리를 다시 붙여줌
		board[head[0]][head[1]] += 1
		snake.append(head)
	else:
		board[head[0]][head[1]] = 2
		snake.append(head)
	# for i in board:
	# 	print(i)
	# print("total_time :", total_time)
	# print("snake :", snake, snake_move)
	# print("")

	if game_over == 1: # 게임이 끝났을 때
		break
	if idx < len(l_lst) and (total_time == l_lst[idx][0]) and (l_lst[idx][1] == 'D'): # 오른쪽으로 가는 경우
		snake_move = (snake_move + 1) % 4
		idx += 1
	elif idx < len(l_lst) and (total_time == l_lst[idx][0]) and (l_lst[idx][1] == 'L'): # 왼쪽으로 가는경우
		snake_move = (snake_move + 4 - 1) % 4
		idx += 1

print(total_time)
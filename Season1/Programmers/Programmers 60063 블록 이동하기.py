from collections import deque

def get_next_pos(pos, board):
	next_pos = [] # 이동 가능한 위치들
	pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]

	move = [(0, -1), (-1, 0), (0, 1), (1, 0)] # 왼, 위, 오, 아
	for i in move:
		dx, dy = i
		pos1_next_x, pos1_next_y, pos2_next_x, pos2_next_y = pos1_x + dx, pos1_y + dy, pos2_x + dx, pos2_y + dy

		if board[pos1_next_x][pos1_next_y] == 0 and board[pos2_next_x][pos2_next_y] == 0:
			next_pos.append([(pos1_next_x, pos1_next_y), (pos2_next_x, pos2_next_y)])
	if pos1_x == pos2_x:
		for i in [-1, 1]: # 위로 회전하거나, 아래로 회전
			if board[pos1_x + i][pos1_y] == 0 and board[pos2_x + i][pos2_y] == 0:
				next_pos.append([(pos1_x, pos1_y), (pos1_x + i, pos1_y)])
				next_pos.append([(pos2_x, pos2_y), (pos2_x + i, pos2_y)])
	elif pos1_y == pos2_y:
		for i in [-1, 1]: # 왼쪽으로 회전하거나, 오른쪽으로 회전
			if board[pos1_x][pos1_y + i] == 0 and board[pos2_x][pos2_y + i] == 0:
				next_pos.append([(pos1_x, pos1_y), (pos1_x, pos1_y + i)])
				next_pos.append([(pos2_x, pos2_y), (pos2_x, pos2_y + i)])
	return next_pos

def solution(board):
	n = len(board)
	new_board = [[1] * (n + 2) for _ in range(n + 2)] # 테두리 넣어주기
	for i in range(n):
		for j in range(n):
			new_board[i + 1][j + 1] = board[i][j]		
	
	q = deque()
	visited = []
	start = [(1, 1), (1, 2)] # 시작위치
	q.append((start, 0))
	visited.append(start)

	while q:
		pos, cost = q.popleft()
		if (n, n) in pos: # 끝나는 위치에 도달할 경우
			return cost
		
		for next_pos in get_next_pos(pos, new_board):
			if next_pos not in visited: # 만약 아직 방문을 하지 않은 경우라면 
				q.append((next_pos, cost + 1))
				visited.append(next_pos)
	return 0

move =[(0, -1), (-1, 0), (0, 1), (1, 0)] # 왼, 위, 오, 아


result = solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]])
print(result)
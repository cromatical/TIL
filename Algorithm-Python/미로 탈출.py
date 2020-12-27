

from collections import deque

n, m = map(int, input().split()) 

mat = [] # n * m 맵 만들기
for _ in range(n):
	mat.append(list(map(int, input())))
# print(mat)

visited = [] # 방문 맵 만들기.
for _ in range(n):
	visited.append([False for _ in range(m)])
# print(visited)

def solution(mat, visited, n, m): # bfs함수
	queue = deque([[0, 0]]) # user 시작 위치
	action_list = [[0, 1], [1, 0], [0, -1], [-1, 0]] # 유저가 움직일 수 있는 액션 [오른쪽, 아래, 왼쪽, 위]

	visited[0][0] = True # 처음 위치 방문 표시
	
	while queue: # 미로 탈출 시작
		v = queue.popleft() # 처음 들어간 위치 확인
		for action in action_list: # 유저가 움직일 수 있는 위치 파악
			r = v[0] + action[0]
			c = v[1] + action[1]
			if r < 0 or r >= n or c < 0 or c >= m: # 맵을 벗어난 경우 
				continue
			else:
				if (not visited[r][c]) and (mat[r][c] == 1): # 방문을 안했고 유저가 움직인 위치가 괴물이 없는 경우
					visited[r][c] = True # 방문 표시로 하고
					queue.append([r, c]) # 큐에 추가
					mat[r][c] = mat[v[0]][v[1]] + 1 # 해당 위치 1 더해주기.
	# print(mat)
	# print(visited)
	return (mat[n - 1][m - 1])

print(solution(mat, visited, n, m))

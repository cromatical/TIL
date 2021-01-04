#

from collections import deque

n, m = map(int, input().split())

lst = []
for _ in range(m):
	lst.append(list(map(int, input().split())))
# print(lst)

def find_num(array, n, m, num): 
	lst = []
	for i in range(m):
		for j in range(n):
			if array[i][j] == num:
				lst.append([i, j])
	if len(lst) == 0:
		return 0
	return lst

def solution(array, n , m):
	if find_num(array, n, m, 0) == 0: # 처음부터 토마토가 전부 익어있는 경우
		return 0
	queue = deque(find_num(array, n, m, 1))
	# print(queue)
	action_lst = [[0, 1], [1, 0], [-1, 0], [0, -1]] # 토마토가 익어가는 방향

	day = 0
	cnt = len(queue) # 첫날 토마토 위치 확인
	while queue:
		val = queue.popleft() # queue에 들어간 원소 하나 팝

		for action in action_lst: # 팝을 한 원소가 움직일 수 있는 경우들
			r = val[0] + action[0]
			c = val[1] + action[1]
			# print(r, c)
			if (r >= 0 and r < m and c >= 0 and c < n) and (array[r][c] == 0):
				array[r][c] = 1 # 토마토 익었다.
				queue.append([r, c]) # queue 추가
		
		cnt -= 1 # 하나의 들어간 원소에 대해 -1
		if cnt == 0: # 0일 경우 첫째날에 해당되는 원소들은 끝!
			cnt = len(queue) # cnt 초기화
			day += 1 # day 추가!	

	if find_num(array, n, m, 0) != 0: # 토마토가 전부다 익을수가 없는 경우.
		return -1
	return day - 1 # 마지막에 queue가 전부 비워지면서 day+1을 해줘서 -1을 해줌

print(solution(lst, n, m))

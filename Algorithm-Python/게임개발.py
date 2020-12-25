# 게임 케릭터가 맵 안에서 움직이는 시스템을 개발중
# 맵은 n x m으로 구성
# 칸은 육지(0)와 바다(1)로 구성
# 케릭터는 상하좌우를 움직일 수 있고 방향을 동, 서, 남, 북을 바라본다.
# 1. 케릭터의 위치는 (a, b)이며, d방향을 본다.
# 2. 현재 방향을 기준으로 왼쪽 방향부터 갈 곳을 정한다.
# 3. 케릭터의 왼쪽 방향에 가보지 않은 칸이 존재하면 왼쪽 방향으로 회전한 다음 왼쪽으로 한칸 전진. 아닐 경우 회전만
# 4. 네 방향 모두 가본칸이거나 바다로 되어 있는 칸인 경우에는, 바라보는 방향을 유지한 채로 뒤로 한칸 돌아간다. 이 때 뒤쪽이 바다면 움직임을 멈춘다.

n , m =  map(int, input().split()) # n x m 맵
a, b, d = map(int, input().split()) # user 위치 (a, b) , d 방향

game_map = [] # 게임 맵
for i in range(n):
	game_map.append(list(map(int, input().split())))
# print(game_map, d)

map_check = [] # 유저가 방문한 칸 확인
for i in range(n):
	map_check.append(['No' for j in range(m)])

user_move = [[-1, 0], [0, 1], [1, 0], [0, -1]] # 파라미터(북, 동, 남, 서)
check = 0
cnt = 1
user_r, user_c = a, b
map_check[user_r][user_c] = 'Yes'

while True: # 유저가 더이상 갈곳이 없을 때 까지
	print(map_check, d)
	d += 1
	if (d > 3): # 4방향 체크
		d = 0

	if (game_map[user_r + user_move[d][0]][user_c + user_move[d][1]] == 0) and (map_check[user_r + user_move[d][0]][user_c + user_move[d][1]] == 'No'): # 맵이 육지고, 유저가 방문하지 않은 곳인 경우
		user_r, user_c = user_r + user_move[d][0], user_c + user_move[d][1] 
		map_check[user_r][user_c] = 'Yes' # 방문으로 바꿈
		cnt += 1 # 방문칸 카운트
		check = 0 
	else:
		check += 1

	if check == 4: # 4방향 전부 확인되었을 떄
		d -= 1 # 원래 보던 방향으로 변환
		if (d == -1):
			d = 3
		# d = (d - 2) % 4
		if game_map[user_r - user_move[d][0]][user_c - user_move[d][1]] == 1: # 뒤로 움직인 방향이 바다면 움직임을 멈춘다.
			break
		user_r, user_c = user_r - user_move[d][0], user_c - user_move[d][1] # 아닐경우에는 뒤로 한칸 움직인다.

print(map_check)
print(game_map)
print(cnt)

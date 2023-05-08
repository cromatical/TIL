# n x m 크기의 얼음틀이 있다.
# 구멍이 뚫려 있는 부분은 0, 칸막이가 있는 부분은 1로 표시되어있다.
# 구멍이 뚫려 있는 부분끼리 서로 연결되어있는 것으로 간주하여 총 생성되는 얼음의 개수를 구하여라.

def solution(lst, i, j): # 탐색
	if (i >= n or j >= m or j <= -1): # 범위를 벗어난 경우
		return 0	
	if lst[i][j] == 0: # 구멍 경우 
		lst[i][j] = 1  # 구멍 부분을 1로 변경
		solution(lst, i, j + 1) # 오른쪽 확인
		solution(lst, i, j - 1) # 왼쪽 확인
		solution(lst, i + 1, j) # 아래 확인
		return 1
	return 0

n, m = map(int, input().split()) # n x m 

lst = [] # 맵 생성
for i in range(n):
	lst.append(list(map(int, input())))
# print(lst)

cnt = 0 # 얼음 개수

for i in range(n): # 탐색
	for j in range(m):
		cnt += solution(lst, i, j) # 현재위치에서 탐색
		# print(lst)
print(cnt)
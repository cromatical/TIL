import sys
input = sys.stdin.readline

n = int(input()) # 삼각형의 크기

table = [] # 테이블 초기값
for i in range(n):
	table.append(list(map(int, input().split())))

memo = [table[0]] # 총합 저장을 위한 메모테이블
for i in range(1, n):
	memo.append([0 for _ in range(len(table[i]))])

for i in memo:
	print(i)
print(i)

for i in range(1, n): # 동적프로그래밍 시작
	for idx, j in enumerate(table[i]):
		# 왼쪽 위의 값
		if idx == 0:
			left_num = 0
		else:
			left_num = memo[i - 1][idx - 1]
		# 오른쪽 위의 값
		if idx == len(table[i]) - 1:
			right_num = 0
		else:
			right_num = memo[i - 1][idx]
		memo[i][idx] = table[i][idx] + max(left_num, right_num)

# memo table 확인
for i in memo:
	print(i)
print("")

# 밑으로 더해져 내려갔을 때 가장큰 값
print(max(memo[-1]))
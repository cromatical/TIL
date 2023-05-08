import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
	n, m = map(int, input().split()) # 금광의 사이즈
	lst = list(map(int, input().split())) # 금광에 들어가는 값

	memo = []
	idx = 0
	for _ in range(n):
		memo.append(lst[idx:idx + m])
		idx += m

	for i in range(1, m):
		for j in range(n):
			# 왼쪽 위에서 오는 경우
			if j == 0:
				left_up = 0
			else:
				left_up = memo[j - 1][i - 1]
			# 왼쪽 아래에서 오는 경우
			if j == n - 1:
				left_down = 0
			else:
				left_down = memo[j + 1][i - 1]
			# 왼쪽에서 오는 경우
			left = memo[j][i - 1]
			memo[j][i] = memo[j][i] + max(left_up, left_down, left)
	result = 0
	for i in range(n):
		result = max(result, memo[i][m - 1])
	print(result) 
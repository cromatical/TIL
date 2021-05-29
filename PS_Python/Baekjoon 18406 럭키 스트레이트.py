import sys
input = sys.stdin.readline

n = input() # 입력
a = len(n) // 2 # 중간을 기준으로
num1 = sum(map(int, n[:a])) # 왼쪽 합
num2 = sum(map(int, n[a:-1])) # 오른쪽 합
if num1 == num2: # 비교
	print("LUCKY")
else:
	print("READY")
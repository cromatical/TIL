# 어떤수 N이 1이 될 때까지 다음 두 과정 중 하나를 반복적으로 수행한다.
# 단, 두번째 연산은 N이 K로 나누어 떨어질 때만 선택가능.
# 1. N에서 1을 뺀다.
# 2. N을 K로 나눈다.
# N과 K가 주어질 때 N이 1이 될 때까지 1번 또는 2번의 과정을 수행하는 최소 횟수를 구하라.

n, k = map(int, input().split())

cnt = 0
while (n != 1): # n이 1이 되면 스탑
	if n % k == 0: # n이 k로 나눠질 때
		n /= k
	else: 
		n -= 1
	cnt += 1
print(cnt)

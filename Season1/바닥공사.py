n = int(input())

# dp가 아닌 규칙을 찾아서
# 1 3 5 11 21 43 ... 
# 짝수번째 경우의 수를 구할 떄 이전값 x 2 + 1
# 홀수번째 경우의 수를 구할 때 이전값 x 2 - 1 

def solution(n):
	if n == 1:
		return 1
	if n % 2 == 0:
		return solution(n - 1) * 2 + 1
	else:
		return solution(n - 1) * 2 - 1

print(solution(n))


# dp테이블 초기화
d = [0] * 1001

d[1] = 1
d[2] = 3
for i in range(3, n + 1):
	d[i] = (d[n - 1] + 2 * d[n - 2]) % 796796

print(d[n])
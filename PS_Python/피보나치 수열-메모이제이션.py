d = [0] * 100 # 한 번 계산된 결과를 메모이제이션하기 위한 리스트 초기화

# 재귀를 이용
def solution(x):
	print(x, end=" ")
	if x == 1 or x == 2: # 재귀함수의 종료조건
		return 1
	if d[x] != 0: # 이미 계산한적 있는 문제하면 그대로 반환
		return d[x]
	d[x] = solution(x - 1) + solution(x - 2) # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
	# solution(5) + solution(4)
	return d[x]

print(solution(6))

# 반복문을 이용
d = [0] * 100 # 마찬가지로 앞서 계산된 결과를 저장하기 위한 dp테이블 초기화

d[1] = 1 # 첫번째 피보나치 수와 두번째 피보나치 수는 1
d[2] = 1
n = 99

for i in range(3, n): # 피보나치 함수 반복문으로 구현
	d[i] = d[i - 1] + d[i - 2]

# print(d[n])
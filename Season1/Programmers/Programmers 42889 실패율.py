import sys
from collections import deque
input = sys.stdin.readline

def solution(N, stages):
	n = N 
	if n < max(stages): # 스테이지와 사용자가 도전한 단게중 큰걸 선택
		n = max(stages)
	result = [[i, 0] for i in range(n + 1)] # 스테이지, 유저 테이블 초기화
	# print(result)

	for i in stages: # 헤당 유저 카운트
		result[i][1] += 1
	# print(result)

	people = len(stages)
	for i in range(1, N + 1): # 실패율 구하기
		if people == 0: # 도전하는 사람이 없을 때 실패율 0 으로 초기화
			result[i][1] = 0
			continue
		fail = result[i][1]
		result[i][1] = result[i][1] / people
		people -= fail
	# print(result)
	result = result[1:N + 1]
	result.sort(key=lambda x: x[1], reverse=True)
	# print(result)
	return [i[0] for i in result]

# N = 5	
# stages = [2, 1, 2, 6, 2, 4, 3, 3]

# N = 4
# stages = [4, 4, 4, 4, 4]

N=8 
stages=[1,2,3,4,5,6,7]
print(solution(N, stages))


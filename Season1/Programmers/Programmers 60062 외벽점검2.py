from itertools import permutations

def solution(n, weak, dist):

	length = len(weak)
	for i in range(length): # 길이 2배로 늘려줌
		weak.append(weak[i] + n)

	answer = len(dist) + 1

	for start in range(len(weak)): # 0 ~ length - 1 까지의 위치를 각각 시작점으로 설정
		for friend in list(permutations(dist, len(dist))): # 친구를 나열하는 모든 경우의 수 각각에 대하여 확인
			count = 1
			position = weak[start] + friend[count - 1]

			for idx in range(start, start + length): # 시작점부터 모든 취약 지점을 확인			
				if position < weak[idx]:
					count += 1
					if count > len(dist):
						break
					position = weak[idx] + friend[count - 1]
			answer = min(answer, count) # 최솟값 계산
	if answer > len(dist):
		return -1
	return answer


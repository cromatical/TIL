def solution(lst, i, cnt):
	print(lst, "점프 횟수 :", cnt, "징검다리 위치 :", i, "점프거리 :", lst[i])
	if lst[-1] == i: # 마지막 징검다리 도착
		return cnt

	if (len(lst) < i) or (i > 0): # 범위를 벗어 날 때
		return -1
	else:
		if not lst[i]: # 0일 때 움직일수 없는 경우
			return -1  
		if (not len(lst) < i) and (not i > 0):
			i += lst[i]
			solution(lst, i, cnt + 1)
			i -= lst[i]
			solution(lst, i, cnt + 1)


lst = list(map(int, input().split()))

print(solution(lst, 0, 0))
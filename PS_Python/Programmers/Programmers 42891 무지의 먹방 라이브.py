def solution(food_times, k):
	i = 0 
	time = 0
	while time < k: # k번째에 장애가 발생하므로 그 전까지 먹음
		while food_times[i] == 0: # 먹어야 할 위치에 음식이 없는 경우 다음 테이블로 이동
			i += 1
			if i >= len(food_times):
				i %= len(food_times)
			if len(set(food_times)) == 1 and set(food_times) == {0}: # 더이상 먹을께 없는 경우
				return -1
		food_times[i] -= 1
		i += 1
		if i >= len(food_times):
			i %= len(food_times)
		time += 1

	while food_times[i] == 0: # 0일 경우 다음 먹을 위치 확인
		i += 1
		if i >= len(food_times):
			i %= len(food_times)
		if len(set(food_times)) == 1 and set(food_times) == {0}: # 더이상 먹을께 없는 경우
			return -1
	return i + 1
	
print(solution([1, 1, 1, 1], 4))
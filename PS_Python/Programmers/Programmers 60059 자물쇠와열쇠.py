import copy

def rotate(lst): # 90, 180 ,270 
	new_key = []
	for i in range(len(lst)):
		row = []
		for j in range(len(lst) - 1, -1, -1):
			row.append(lst[j][i])
		new_key.append(row)
	return new_key

def solution(key, lock):
	# print(key, lock)
	rotation_lst = [key]
	for i in range(3): # 90, 180, 270
		rotation_lst.append(rotate(rotation_lst[i]))
	
	# for i in rotation_lst:
	# 	print("i :", i)

	padding_length = len(lock) - 1
	total_length = len(lock) + padding_length * 2
	padding_lock = [[0] * total_length for _ in range(total_length)]
	# print(padding_lock) 58 * 58  

	for i in range(len(lock)):
		for j in range(len(lock)):
			padding_lock[i + total_length // 2 - 1][j + total_length // 2 - 1] = lock[i][j]
	# for i in padding_lock:
	# 	print(i)

	for lst in rotation_lst: # 0, 90, 180, 270 값 불러오기.
		for r in range(total_length - len(key) + 1): # 전체 패딩된 맵 불러오는 용도
			for c in range(total_length - len(key) + 1):
				result_lock = copy.deepcopy(padding_lock) # padding_lock은 계속 사용하기 때문에
				for i in range(len(key)): # key에 해당되는 부분
					for j in range(len(key)):
						result_lock[i + r][j + c] += lst[i][j]
				# for result in result_lock:
				# 	print(result)

				cnt = 0
				for i in range(len(lock)):
					for j in range(len(lock)):
						if result_lock[i + total_length // 2 - 1][j + total_length // 2 - 1] == 1:
							cnt += 1
				# print(cnt)	
				if cnt == len(lock) * len(lock):
					return True
				# print("")

	return False


key = [[[0, 0, 0], [1, 0, 0], [0, 1, 1]]]
lock = [[[1, 1, 1], [1, 1, 0], [1, 0, 1]]]
for i in range(len(key)):
	print(solution(key[i], lock[i]))
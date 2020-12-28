array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)): # 삽입정렬에서는 항상 제일 처음 인덱스는 정렬이 되어있다 가정한다.
	for j in range(i, 0, -1): # 한칸씩 왼쪽으로 이동
		if array[j] < array[j - 1]: # 작으면 스왑
			array[j], array[j - 1] = array[j - 1], array[j]
		else:
			break
print(array)
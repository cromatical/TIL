array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)): 
	min_val = i # i번째 인덱스 위치에 값을 저장
	for j in range(i, len(array)): # i다음 인덱스부터 차례대로 확인
		if array[min_val] > array[j]: # 만약 j가 i번째 인덱스 값보다 작다면 
			min_val = j
	array[i], array[min_val] = array[min_val], array[i] # 스왑!
print(array)
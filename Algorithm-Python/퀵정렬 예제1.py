array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def solution(array, start, end):
	if start >= end: # 리스트 개수가 하나인 경우 스탑
		return
	pivot = start # 첫 번째 인덱스를 피벗으로 설정
	left = start + 1
	right = end

	while (left <= right):
		while (left <= end and array[left] <= array[pivot]): # 피벗보다 큰 데이터를 찾을 때까지 반복
			left += 1
		while (right > start and array[right] >= array[pivot]): # 피벗보다 작은 데이터를 찾을 때까지 반복
			right -= 1
		if left > right: # left와 right가 엇갈린 경우 가장 작은 데이터와 피벗을 스왑
			array[right], array[pivot] = array[pivot], array[right]
		else:
			array[left], array[right] = array[right], array[left]
	solution(array, start, right - 1) # 왼쪽부분 다시 퀵정렬
	solution(array, right + 1, end) # 오른쪽부분 다시 퀵정렬 

solution(array, 0, len(array) - 1)
print(array)
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def solution(array):
	if len(array) <= 1: # 리스트가 하나 이하의 원소만을 담고 있다면 종료
		return array
	
	pivot = array[0] # 가장 왼쪽을 피벗으로 설정
	tail = array[1:] # 피벗을 제외한 리스트

	left = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
	right = [x for x in tail if x > pivot] # 분활된 오른쪽 부분

	return  solution(left) + [pivot] + solution(right)

print(solution(array))
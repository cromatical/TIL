n, x = map(int, input().split()) # n개의 원소, 숫자 x
num_lst = list(map(int, input().split())) # 오름차순으로 정렬된 수열 테이블

def first_b_search(array, target, start, end): # 숫자 x의 첫번째 인덱스를 찾는 함수
	if start > end:
		return None
	mid = (start + end) // 2
	if (mid == 0 or target > array[mid - 1]) and array[mid] == target: # mid == 0 또는 target보다 앞의 인덱스가 작고, 미드인덱스의 값이 target일 때
		return mid
	elif array[mid] >= target: # target이 mid보다 작거나 같으면 왼쪽으로 이동
		return first_b_search(array, target, start, mid - 1)
	else:
		return first_b_search(array, target, mid + 1, end)

def last_b_search(array, target, start, end): # 숫자 x의 마지막 인덱스를 찾는 함수
	if start > end:
		return None
	mid = (start + end) // 2
	if (mid == n - 1 or target < array[mid + 1]) and array[mid] == target:
		return mid
	elif array[mid] > target:
		return last_b_search(array, target, start, mid - 1)
	else:
		return last_b_search(array, target, mid + 1, end)

num1 = first_b_search(num_lst, x, 0, n - 1)
num2 = last_b_search(num_lst, x, 0, n - 1)
if num1 == None and num2 == None:
	print(-1)
else:
	print(num2 - num1 + 1)
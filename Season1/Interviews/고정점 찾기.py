def b_search(array, start, end):
	if start > end:
		return None
	mid = (start + end) // 2

	# print(start, end, mid)
	if array[mid] == mid: # 고정점을 찾은 경우
		return mid
	elif array[mid] > mid: # 고정점보다 작은 경우
		return b_search(array, start, mid - 1)
	else: # 고정점 보다 큰 경우
		return b_search(array, mid + 1, end)

n = int(input()) # 입력받을 숫자의 개수
lst = list(map(int, input().split())) # 원소가 들어간 테이블

result = b_search(lst, 0, n - 1) # 이진탐색
if result != None: # 고정점이 있는 경우
	print(result)
else:
	print(-1)
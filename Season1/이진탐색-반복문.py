def solution(array, target, start, end):
	while start < end:
		mid = (start + end) // 2

		if array[mid] == target:
			return mid
		elif array[mid] > target:
			end = mid - 1
		else:
			start = mid + 1
	return None

# 원소의 개수 n과 찾고자 하는 수 target 입력
n, target = list(map(int, input().split()))

# 전체 원소 입력
array = list(map(int, input().split()))

# 이진탐색 수행 결과
result = solution(array, target, 0, n - 1)
if result == None:
	print("찾고자하는 원소가 없습니다.")
else:
	print(result + 1)
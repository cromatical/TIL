def solution(array, target, start, end):
	if start > end:
		return None
	mid = (start + end) // 2 # 중간지점 확인
	if array[mid] == target: # 찾고자 하는게 중간지점인지 확인
		return mid
	elif array[mid] > target: # 찾고자 하는게 mid보다 큰 경우
		return solution(array, target, start, mid - 1)
	else: # mid보다 작은 경우
		return solution(array, target, mid + 1, end)

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
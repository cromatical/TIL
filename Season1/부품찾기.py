# 전자매장에 N개의 부품이 있다. 각 부품은 정수형태의 고유번호를 가진다.
# 어느날 손님이 M개의 부품을 구매하겠다고 요청했다
# 전자매장에 손님이 찾을 M개의 부품이 있는지 확인하는 프로그램을 작성하자.
# 부품이 존재하면 'Yes', 없다면 'No'로 출력한다.


n = int(input()) # 상점에서 파는 부품 n개
store_lst = list(map(int, input().split())) 

m = int(input()) # 손님이 원하는 부품 m개
guest_lst = list(map(int, input().split()))

print(n, store_lst)
print(m, guest_lst)

store_lst.sort() # 이진탐색을 위해 정렬

# 2 3 7 8 9 
# 5 7 9

def solution(array, target, start, end): # 이진탐색 함수
	if start > end:
		return None
	mid = (start + end) // 2
	if array[mid] == target:
		return mid
	elif array[mid] > target:
		return solution(array, target, start, mid - 1)
	else:
		return solution(array, target, mid + 1, end)

answer_lst = [] # 가지고 있는지 확인을 위한 리스트
for target in guest_lst:
	result = solution(store_lst, target, 0, n - 1) # 이진탐색 시작
	if result != None:
		answer_lst.append("Yes")
	else:
		answer_lst.append("No")

print(answer_lst)	
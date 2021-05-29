# 피보나치 함수 재귀로 구현
def fibo(x):
	if x <= 1:
		return 1
	return fibo(x - 2) + fibo(x - 1)

# print(fibo(1))
# print(fibo(2))
# print(fibo(3))
# print(fibo(4))
# print(fibo(5))

# 피보나치 메모이제이션
memo = [0] * 100

def fibo2(x):
	if x <= 1:
		return 1
	if memo[x] != 0:
		return memo[x]
	memo[x] = fibo(x - 2) + fibo(x - 1)
	return memo[x]

# print(fibo2(0))
# print(fibo2(1))
# print(fibo2(2))
# print(fibo2(3))
# print(fibo2(4))
# print(fibo2(5))

# 재귀를 이용한 팩토리얼
def facto(x):
	if x == 1:
		return 1
	return x * facto(x - 1)

import random

# 10번 동안 1 ~ 10 까지 랜덤한 숫자를 출력하여 중복된 숫자가 있을 경우 true, false를 리턴

# lst = [random.randrange(1, 10) for i in range(10)]

# dic = {}
# for i in lst:
# 	if dic.get(i) == None:
# 		dic[i] = 1
# 	else:
# 		dic[i] += 1

# for key, value in dic.items():
# 	if value > 1:
# 		return True
# return False
		
# 각종 정렬

lst = [7, 5, 9, 0, 3, 1, 6, 2, 4 ,8]
print(lst)
# 선택정렬

# for i in range(len(lst)):
# 	for j in range(i + 1, len(lst)):
# 		if lst[j] < lst[i]:
# 			lst[j], lst[i] = lst[i], lst[j]
# print(lst)

# 삽입정렬

# for i in range(1, len(lst)):
# 	for j in range(i, 0, -1):
# 		if lst[j - 1] > lst[j]:
# 			lst[j], lst[j - 1] = lst[j - 1], lst[j]
# 		else:
# 			break
# print(lst)

# 버블정렬

for i in range(len(lst)):
	for j in range(len(lst) - i - 1):
		if lst[j] > lst[j + 1]:
			lst[j], lst[j + 1] = lst[j + 1], lst[j]
print(lst)

# 힙정렬
# 힙의 성질을 만족하는지 확인
def heapify(unsorted, index, heap_size):
	largest = index
	left_idx = 2 * index + 1
	right_idx = 2 * index + 2
	if left_idx < heap_size and unsorted[left_idx] > unsorted[largest]:
		largest = left_idx
	if right_idx < heap_size and unsorted[right_idx] > unsorted[largest]:
		largest = right_idx
	if largest != index:
		unsorted[largest], unsorted[index] = unsorted[index], insorted[largest]
		heapify(unsorted, largest, heap_size)

def heap_sort(unsorted):
	n = len(unsorted)
	# 부모는 자식보다 크다는 힙성질이 있어서 중간부터 시작한다.
	# 우선 주어진 원소들로 최대힙을 구성한다.
	for i in range(n // 2 - 1, -1, -1):
		heapify(unsorted, i, n)
	# 정렬 수행하자
	# 최대힙의 루트노드와 말단 노드를 교환해준다.
	# 새 루트노드에 대해 최대힙을 구성한다.
	# 원소의 개수만큼 반복
	for i in range(n - 1, 0, -1):
		unsorted[0], unsorted[i] = unsorted[i], unsorted[0]
		heapify(unsorted, 0, i)

def quick_sort(array):
	if len(array) <= 1:
		return array
	
	pivot = array[0]
	tail = array[1:]

	left_array = [x for x in tail if x <= pivot]
	right_array = [x for x in tail if x > pivot]

	return quick_sort(left_array) + [pivot] + quick_sort(right_array)


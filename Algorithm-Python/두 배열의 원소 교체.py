# 두 배열은 n개의 원소를 가지고 있다.
# b에서 k횟수 만큼 옮길수가 있다.
# 배열 a의 합이 가장 큰 값을 가지도록 코드를 구현하라.

n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
print("정렬 전 : ", a)
print("정렬 전 : ", b)

def solution(array): # 퀵정렬 정의
	if len(array) <= 1:
		return array
	
	pivot = array[0]
	tail = array[1:]

	left = [i for i in tail if i <= pivot]
	right = [i for i in tail if i > pivot]

	return solution(left) + [pivot] + solution(right)

new_a = solution(a)
new_b = solution(b)
print("정렬 후 : ", new_a)
print("정렬 후 : ", new_b)


a_idx = 0 # a 배열 초기 인덱스
b_idx = len(new_b) - 1 # b배열 마지막 인덱스

result = 0 # 합을 구하기 위한 변수

if len(new_a) == 0: # 배열 a가 비어있을 때, 배열 b가 비어있을 때는 굳이 할 필요가 없다.
	for _ in range(k): # k만큼!
		val = new_b.pop()
		new_a.append(val)	
else: # 배열 a의 0번째 인덱스와, 배열 b의 마지막 인덱스를 비교하여 만약 배열b의 값이 더 클 경우 스왑.
	for _ in range(k): # k만큼!
		# [1, 2, 3, 4, 5]
		# [5, 5]
		# k = 3
		if (new_a[a_idx] < new_b[b_idx] and b_idx > -1 and a_idx < len(new_a) - 1):
			new_a[a_idx], new_b[b_idx] = new_b[b_idx], new_b[b_idx]
			a_idx += 1
			b_idx -= 1
		else:
			break

result = sum(new_a)
print(result)
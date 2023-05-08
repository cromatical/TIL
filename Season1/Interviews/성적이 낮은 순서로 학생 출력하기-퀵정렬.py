n = int(input())

lst = []
for _ in range(n):
	a, b = input().split()
	lst.append([a, int(b)])
print(lst)

def solution(lst):
	if len(lst) <= 1: # 리스트의 길이가 1이면 스탑
		return lst
	
	pivot = lst[0] # 가장 왼쪽을 피벗으로 지정
	tail = lst[1:] # 피벗 이후 쭉~~

	left = [x for x in tail if x[1] <= pivot[1]] # 피벗보다 같거나 작은 경우 왼쪽으로
	right = [x for x in tail if x[1] > pivot[1]] # 피벗보다 클 경우 오른쪽으로

	return solution(left) + [pivot] +  solution(right)

print(' '.join(i[0] for i in solution(lst)))
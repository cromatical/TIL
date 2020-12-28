n = int(input())

lst = {} # 딕셔너리 생성
for _ in range(n):
	name, score = input().split()
	lst[name] = int(score)
# print(lst)

def solution(lst):
	cnt_lst = [ 0 for _ in range(max(lst.values()) + 1)] # 0~100점 이므로 101개의 공간을 가진 빈 리스트 생성
	sort_lst = [ 0 for _ in range(len(lst))] # 정렬을 위한 리스트 생성

	for i in lst.values(): # 해당점수 인덱스에 카운트
		cnt_lst[i] += 1
	
	for i in range(1, max(lst.values()) + 1): # cnt 누적 덧셈
		cnt_lst[i] += cnt_lst[i - 1]
	
	for k, v in lst.items():
		sort_lst[cnt_lst[v] - 1] = (k, v) # cnt에서의 총합의 값 sort_lst인덱스와 비교하면 1크다
		cnt_lst[v] -= 1 # lst의 값 하나를 빼줬으므로 -1
	
	return sort_lst

print(solution(lst))
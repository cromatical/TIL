# 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.
# 길이가 짧은 것부터
# 길이가 같으면 사전 순으로
# 입력받은것 중 중복이 있으면 제거.

n = int(input())
lst = [input() for _ in range(n)]

lst1 = []
for i in lst:
	if not i in lst1:
		lst1.append(i)
# print(lst1)
		
def solution(data): # 정렬 정의 1
	return len(data)

sort_lst = sorted(lst1, key=solution) # 길이로 정렬
print(sort_lst)

def solution2(a, b, i): # 알파벳 하나하나씩 비교하여 정렬 하는 함수 아스키를 이용!
	if i == len(a):
		return a, b
	if a[i] != b[i]:
		if ord(a[i]) > ord(b[i]): # 아스키값 비교
			return b, a
		return a, b
	return solution2(a, b, i + 1) # a, b 의 값이 계속 같을 경우 인덱스를 증가시켜 다시 

length = len(sort_lst) # 버블정렬 응용
for i in range(length - 1):
	for j in range(length - i - 1):
		a = sort_lst[j]
		b = sort_lst[j + 1]
		if (len(a) == len(b)): # 길이가 같을 경우 아스키 값을 이용하여 정렬
			sort_lst[j], sort_lst[j + 1] = solution2(a, b, 0)
		
print(sort_lst)
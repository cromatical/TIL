# n개의 수열을 입력받아서 이 수열을 내림차순으로 정렬하시오.

n = int(input())

lst = [] # 입력값 저장할 리스트
for _ in range(n):
	lst.append(int(input()))

lst.sort() # 오름차순
lst.reverse() # 반전

print(' '.join(map(str, lst))) # 문자열로 바꾼뒤 변환
import sys
input = sys.stdin.readline

n = int(input()) # 집의 개수
house_lst = list(map(int, input().split()))

house_lst.sort()

result_lst = []
for i in range(n):
	point = house_lst[i]
	result = sum(list(map(lambda x: abs(x - point), house_lst)))
	result_lst.append(result)
print(min(result_lst))

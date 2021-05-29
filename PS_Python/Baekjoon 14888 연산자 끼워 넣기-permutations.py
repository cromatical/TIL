import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input()) # 숫자개수
num_lst = list(map(int, input().split())) # 숫자 수열.
arithmetic_lst = ['+', '-', '*', '/']
arithmetic_cnt = list(map(int, input().split())) # 연산 리스트, 개수 왼쪽부터 +, - ,*, /

new_arithmetic_lst = [] # 2 1 1 1  [+ + - * /]
for i in range(len(arithmetic_lst)):
	new_arithmetic_lst += arithmetic_lst[i] * arithmetic_cnt[i]
# print(new_arithmetic_lst)

total_lst = list(permutations(new_arithmetic_lst, sum(arithmetic_cnt)))
# print(total_lst)

result_lst = []
for i in total_lst:
	result = num_lst[0]
	for j in range(len(num_lst) - 1):
		if i[j] == '+':
			result += num_lst[j + 1]
		elif i[j] == '-' :
			result -= num_lst[j + 1]
		elif i[j] == '*':
			result *= num_lst[j + 1]
		else:
			negative = 1
			if result < 0:
				negative = -1
				result *= negative
			result = result // num_lst[j + 1]
			result *= negative
	result_lst.append(result)

result_lst.sort(reverse=True)
print(result_lst[0])
print(result_lst[-1])




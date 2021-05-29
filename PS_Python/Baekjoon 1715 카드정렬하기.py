import sys
import heapq
input = sys.stdin.readline

n = int(input())

num_lst = []
for _ in range(n):
	heapq.heappush(num_lst, int(input()))
# print(num_lst)

if len(num_lst) == 1:
	print(0)
else:
	answer = 0
	while len(num_lst) > 1:
		num1 = heapq.heappop(num_lst)
		num2 = heapq.heappop(num_lst)
		answer += num1 + num2
		heapq.heappush(num_lst, num1 + num2)
print(answer)
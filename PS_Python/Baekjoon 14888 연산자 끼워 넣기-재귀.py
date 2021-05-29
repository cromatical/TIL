import sys
sys.setrecursionlimit(500000)
input = sys.stdin.readline

n = int(input()) # 숫자개수 입력
num_lst = list(map(int, input().split())) # 숫자 수열 테이블.
arithmetic_lst = ['+', '-', '*', '/']
arithmetic_cnt = list(map(int, input().split()))

total_lst = []

def solution(num_lst, result, n):
	if n == 1:
		total_lst.append(result)
		return 
	if arithmetic_cnt[0] > 0:
		arithmetic_cnt[0] -= 1
		solution(num_lst[1:],  result + num_lst[0], n - 1)
		arithmetic_cnt[0] += 1
	if arithmetic_cnt[1] > 0:
		arithmetic_cnt[1] -= 1
		solution(num_lst[1:], result - num_lst[0], n - 1)
		arithmetic_cnt[1] += 1
	if arithmetic_cnt[2] > 0:
		arithmetic_cnt[2] -= 1
		solution(num_lst[1:], result * num_lst[0], n - 1)
		arithmetic_cnt[2] += 1	
	if arithmetic_cnt[3] > 0:
		arithmetic_cnt[3] -= 1
		solution(num_lst[1:], int(result / num_lst[0]), n - 1)
		arithmetic_cnt[3] += 1
	return

solution(num_lst[1:], num_lst[0], n)
total_lst.sort(reverse=True)
print(total_lst[0])
print(total_lst[-1])



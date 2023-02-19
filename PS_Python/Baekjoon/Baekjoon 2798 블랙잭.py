# combinations를 통해서 중복된 경우 빼고 나올수 있는 3개의 조합을 구함
# 총 합이 m을 넘어가지 않는 선에서 가장 가까운 3개의 숫자의 총합을 구함

import sys
input = sys.stdin.readline
from itertools import combinations

n, m = map(int, input().split()) 
num_lst = list(map(int, input().split()))

all_case = list(combinations(num_lst, 3))

near_sum = 0

for i in all_case:
	if near_sum < sum(i) <= m:
		near_sum = sum(i)
print(near_sum)
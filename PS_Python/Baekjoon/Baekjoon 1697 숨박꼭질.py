import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split()) # 수빈이 위치, 동생의 위치

def bfs(n, k, cnt):
	q = deque([[n]])
	while (q):
		now = q.popleft()
		lst = []
		for i in now:
			move_lst = [i - 1, i + 1, i * 2]
			for move in move_lst:
				if move == k:
					return cnt
				lst.append(move)
		q.append(lst)
		cnt += 1	

print(bfs(n, k, 1))
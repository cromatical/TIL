import sys
from collections import deque
input = sys.stdin.readline
INF = int(1e9)

v = int(input()) 
indegree = [0] * (v + 1)
graph = [[] for _ in range(v + 1)]
time = [0] * (v + 1)

for i in range(1, v + 1):
	info = list(map(int, input().split()))
	j = 0
	while (info[j] != -1):
		if j == 0:
			time[i] = info[j]
		else:
			graph[info[j]].append(i)
			indegree[i] += 1
		j += 1
	# print(graph)
	# print(time)
	# print(indegree)
print(graph)

def topology_sort():
	time_lst = time[:]
	q = deque()
	
	for i in range(1, v + 1):
		if indegree[i] == 0:
			q.append(i)

	time_lst[1] = time[1]
	while q:
		now = q.popleft()

		for i in graph[now]:
			result = time[i] + time_lst[now] # 누적값을 비교하여 더 큰값을 넣어준다.
			if result > time_lst[i]:
				time_lst[i] = result
			indegree[i] -= 1
			if indegree[i] == 0:
				q.append(i)

	for i in time_lst[1:]: # 위상정렬 결과 출력
		print(i)

topology_sort()


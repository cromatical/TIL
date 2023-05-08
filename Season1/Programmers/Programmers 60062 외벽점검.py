from itertools import combinations

# n = int(input()) # 원형 레스토랑 길이
# res = deque([0] * n) # 레스토랑 외부 벽 길이 테이블
# weak = tuple(map(int, input().split())) # 공사가 필요한 부분
# dist = tuple(map(int, input().split())) # 각 친구들이 움직일 수 있는 칸

def solution(n, weak, dist):
	total_lst = [] 
	for i in range(len(weak)): 
		result = combinations(weak, i)
		total_lst.append([i for i in result])		
	total_lst.append([tuple(weak)])
	total_lst.sort(reverse=True)

	d_lst = []
	for i in total_lst[:-2]:
		length = []
		for j in i:
			if len(j) > 1:
				if not j[-1] - j[0] in length:
					length.append(j[-1] - j[0])
				
				for k in range(len(j)):
					if not (n - j[k + 1] - 1) + j[k] in length:
						length.append((n - j[k + 1] - 1) + j[k])

		length.sort()
		d_lst.append(length)
	d_lst.append([i for i in dist])	 
	print(d_lst)
	print(dist)

	i = 1
	for d in d_lst:
		cnt = 0
		for d2 in dist:
			if d2 in d:
				cnt += 1
		if i == cnt:
			return (cnt - 1)
		i += 1
	return -1

n = 12
weak = [1, 5, 6, 10]
dist = [1, 2, 3, 4]

print(solution(n, weak, dist))
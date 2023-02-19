from itertools import combinations

n, m = map(int, input().split()) 


map_lst = [] # 맵을 저장할 테이블 생성
for _ in range(n):
	map_lst.append(list(map(int, input().split())))

h_lst = [] # 집 위치를 저장할 테이블
c_lst = [] # 치킨집 위치를 저장할 테이블
for i in range(n):
	for j in range(n):
		if map_lst[i][j] == 1: # 집인경우
			h_lst.append((i, j))
		elif map_lst[i][j] == 2: # 치킨집인경우
			c_lst.append((i, j))
	
total_lst = combinations(c_lst, m) # c_lst에 있는 원소로 m개 구성되었을 때 나올수 있는 경우의수
smallest_lst = [] # 도시치킨거리를 저장할 테이블

for new_c_lst in total_lst: # m개만큼 만들어진 경우의수
	d_lst = [] # 해당 치킨집과 집들에서 구할수있는 거리
	for h in h_lst:
		h_to_c = []
		r1, c1 = h
		for c in new_c_lst:
			r2, c2 = c
			result = abs(r1 - r2) + abs(c1 - c2)
			h_to_c.append(result)
		h_to_c.sort()
		d_lst.append(h_to_c[0])
	smallest_lst.append(sum(d_lst))

print(min(smallest_lst))
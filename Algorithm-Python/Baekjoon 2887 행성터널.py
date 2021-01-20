import sys
sys.setrecursionlimit(500000)
input = sys.stdin.readline

n = int(input()) # 행성의 개수 입력
parent = [0] * (n + 1)

for i in range(1, n + 1):
	parent[i] = i

# planet_lst = [[None]]
# for _ in range(n):
# 	x, y, z = map(int, input().split()) # 행성의 좌표
# 	planet_lst.append((x, y, z))

# edge_lst = []
# for i in range(1, n + 1):
# 	for j in range(i + 1, n + 1):
# 		xa, ya, za = planet_lst[i]
# 		xb, yb, zb = planet_lst[j]
# 		cost = min(abs(xa - xb), abs(ya - yb), abs(za - zb))
# 		edge_lst.append((cost, i, j))

# 기존의 방식으로 하면 메모리초과, 시간초과로 인하여 문제를 해결할 수가 없다.
# 문제에서  min(|xA-xB|, |yA-yB|, |zA-zB|)와 같은 조건을 주었기 때문에 각각에 대해서 정렬을 하여 n - 1만큼 간선을 확인하면 된다.

arr_x = []
arr_y = []
arr_z = []

for i in range(1, n + 1):
	x ,y ,z = map(int, input().split())
	arr_x.append((x, i))
	arr_y.append((y, i))
	arr_z.append((z, i))

# 각 좌표에 대해서 정렬
arr_x.sort()
arr_y.sort()
arr_z.sort()

edge_lst = []
for i in range(n - 1): 
	edge_lst.append((abs(arr_x[i + 1][0] - arr_x[i][0]), arr_x[i][1], arr_x[i + 1][1]))
	edge_lst.append((abs(arr_y[i + 1][0] - arr_y[i][0]), arr_y[i][1], arr_y[i + 1][1]))
	edge_lst.append((abs(arr_z[i + 1][0] - arr_z[i][0]), arr_z[i][1], arr_z[i + 1][1]))
	
# 다시 abs기준으로 정렬
edge_lst.sort()

def find_parent(parent, x):
	if x != parent[x]:
		parent[x] = find_parent(parent, parent[x])
	return parent[x]

def union_parent(parent, a ,b):
	a = find_parent(parent, a)
	b = find_parent(parent, b)
	if a < b:
		parent[b] = a
	else:
		parent[a] = b

result = 0
for edge in edge_lst:
	cost, a, b = edge
	if find_parent(parent, a) != find_parent(parent, b):
		union_parent(parent, a, b)
		result += cost
print(result)
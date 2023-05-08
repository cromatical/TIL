import sys
input = sys.stdin.readline

n = int(input())

house_map = []
for i in range(n):
	line = input()
	house_map.append([int(i) for i in line[:-1]])

def dfs(house_map, r, c, cnt):
	if r >= n or r < 0 or c >= n or c < 0:
		return 0
	if house_map[r][c] == 1:
		house_map[r][c] = 0
		return 1 + dfs(house_map, r, c + 1, cnt) + dfs(house_map, r, c - 1, cnt) + dfs(house_map, r + 1, c, cnt) + dfs(house_map, r - 1, c, cnt)
	return 0

result_lst = []
for i in range(n):
	for j in range(n):
		if house_map[i][j] == 1:
			result_lst.append(dfs(house_map, i, j, 0))

print(len(result_lst))
result_lst.sort()
for i in result_lst:
	print(i)
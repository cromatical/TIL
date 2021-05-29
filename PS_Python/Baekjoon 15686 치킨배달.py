n, m = map(int, input().split()) # 도시 사이즈, 남길 치킨집 m개

city_lst = []
for _ in range(n):
	line = list(map(int, input().split())) # 도시입력
	city_lst.append(line)

house_lst = []
chiken_lst = []
for i in range(n): # 집과 치킨집에 해당되는 경우를 파악
	for j in range(n):
		if city_lst[i][j] == 1: # house인 경우
			house_lst.append((i + 1, j + 1))
		elif city_lst[i][j] == 2: # 치킨집인 경우
			chiken_lst.append((i + 1, j + 1))
# print(house_lst)
# print(chiken_lst)


best_chiken_lst = {i:0 for i in chiken_lst}
# print(best_chiken_lst)

for house in house_lst:
	sort_lst = []
	r1, c1 = house
	for chiken in chiken_lst:
		r2, c2 = chiken
		sort_lst.append((abs(r1 - r2) + abs(c1 - c2), chiken))
	sort_lst.sort()
	print(sort_lst)
	for i in range(m - 1, len(sort_lst)):
		best_chiken_lst[sort_lst[i][1]] += i
print(best_chiken_lst)

print(chiken_lst)
# print(best_chiken_lst)
for i in range(len(chiken_lst) - m):
	target = max(best_chiken_lst, key=lambda x: best_chiken_lst[x])
	chiken_lst.remove(target)
	best_chiken_lst[target] = -1
	# print(chiken_lst)
	# print(best_chiken_lst)

print(chiken_lst)

best_sort_lst = []
for house in house_lst:
	sort_lst = []
	r1, c1 = house
	for chiken in chiken_lst:
		r2, c2 = chiken
		sort_lst.append((abs(r1 - r2) + abs(c1 - c2), chiken))
	sort_lst.sort()
	best_sort_lst.append(sort_lst[0])

# print(chiken_lst)
print(best_sort_lst)
print(sum([i[0] for i in best_sort_lst]))

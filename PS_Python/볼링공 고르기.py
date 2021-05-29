n, m = map(int, input().split()) # 볼링공의 개수, 무게의 범위
weight_lst = list(map(int, input().split()))

weight_lst.sort()
# print(weight_lst)
cnt = 0
for i in range(len(weight_lst)): # 볼링공의 무게
	for j in range(i + 1, len(weight_lst)): # 비교해야할 다음 볼링공
		if weight_lst[i] != weight_lst[j]: # 같지 않으면!
			# print(i, j)
			cnt += 1
print(cnt)
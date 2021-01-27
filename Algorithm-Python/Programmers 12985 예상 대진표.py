def solution(n,a,b):
	n = [[i for i in range(1, n + 1)]]
	cnt = 1

	for _ in range(len(n[0]) // 2):
		# print(i, len(n[-1]))
		lst = []
		for j in range(0, len(n[-1]) - 1, 2):
			# print(n[-1], n[-1][j], n[-1][j + 1])
			if (n[-1][j] == a and n[-1][j + 1] == b) or (n[-1][j] == b and n[-1][j + 1] == a):
				return cnt
			if n[-1][j] == a or n[-1][j + 1] == a:
				lst.append(a)
			elif n[-1][j] == b or n[-1][j + 1] == b:
				lst.append(b)
			elif n[-1][j] < n[-1][j + 1]:
				lst.append(n[-1][j])
		n.append(lst)
		cnt += 1
	return cnt

print(solution(8, 3, 7))
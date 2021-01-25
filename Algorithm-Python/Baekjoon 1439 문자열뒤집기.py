import sys
input = sys.stdin.readline

n = list(map(str, input())) # 문자열 입력

def solution(n):
	cnt_0 = 0
	cnt_1 = 0
	i = 0

	while i < len(n):
		j = 0
		if i + j < len(n) and n[i] == n[i + j]:
			while i + j < len(n) and n[i] == n[i + j]:
				j += 1
			if n[i] == '0':
				cnt_0 += 1
			else:
				cnt_1 += 1
			i += j
		else:
			i += 1
	return ('0', cnt_0), ('1', cnt_1)

def solution2(n, c):
	cnt = 0 
	state = 0

	for i in range(len(n)):
		if n[i] != c:
			n[i] = c
			state = 1
		elif n[i] == c and state == 1:
			state = 0
			cnt += 1
	return cnt

cnt = 0
while 1:
	a, b = solution(n)
	if a[1] > b[1]:
		cnt = solution2(n, '0')
	else:
		cnt = solution2(n, '1')
	if len(set(n)) == 1:
		break
print(cnt)
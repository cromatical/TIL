from collections import Counter

n = list(map(str, input()))

def solution(n): # 2개이상 연속으로 사용된 숫자의 덩어리 갯수를 파악해주는 함수
	cnt_0 = 0
	cnt_1 = 0
	i = 0

	while i < len(n):
		start = i + 1
		j = 0
		if start < len(n) and n[start] == n[i + j]:
			while n[start] == n[i + j]:
				j += 1
				if i + j >= len(n):
					j -= 1
					break
			if n[start] == '0':
				cnt_0 += 1
			else:
				cnt_1 += 1
			i += j
		else:
			i += 1

	return ('0', cnt_0), ('1', cnt_1)

def solution2(n, c):
	cnt = 0

	if c == '0':
		check_num = '1'
	else:
		check_num = '0'
	i = 0
	while i < len(n):
		if i + 1 < len(n) and n[i] == check_num and n[i + 1] == check_num:
			start = i
			while n[start] != c:
				n[start] = c
				start += 1
				if start >= len(n):
					return cnt
			cnt += 1
			i += start
		else:
			i += 1
	return cnt

cnt = 0	
while 1:
	cnt_0, cnt_1 = solution(n)
	print(cnt_0, cnt_1)
	if cnt_0[1] == 0:
		a = solution2(n, '0')
		cnt += a
	elif cnt_1[1] == 0:
		a = solution2(n, '1')
		cnt += a
	elif  cnt_0[1] > cnt_1[1]:
		a = solution2(n, '1')
		cnt += a
	else:
		a = solution2(n, '0')
		cnt += a
	if len(set(n)) == 1:
		print(n)
		break
	print(n)
print(cnt)
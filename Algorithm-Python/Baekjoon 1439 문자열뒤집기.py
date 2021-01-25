import sys
input = sys.stdin.readline

n = input() # 문자열 입력

cnt_0 = 0
cnt_1 = 0

if n[0] == '1':
	cnt_0 += 1
else:
	cnt_1 += 1

for i in range(len(n) - 1):
	if n[i] != n[i + 1]:
		if n[i + 1] == '1':
			cnt_0 += 1
		else:
			cnt_1 += 1

print(min(cnt_0, cnt_1))
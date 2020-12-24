# 8 x 8체스판이 있다.
# 체스판 특정칸에 나이트가 있다.
# 나이트는 L형태로만 이동이 가능하고 체스판 밖으로는 나갈수가 없다.
# L형태의 움직임은 다음과 같다.
# 1. 수평 두 칸 이동 뒤 수직으로 한 칸 이동
# 2. 수직 두 칸 이동 뒤 수평으로 한 칸 이동


n = input() # 나이트의 위치

col = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'] # 열에 해당되는 나이트의 위치를 변환

for i in range(8): # 열에 해당되는 숫자로 변환
	if n[0] == col[i]:
		c = i + 1

r = int(n[1]) 

cnt = 0

if (r + 2) < 9 and (c - 1) > 0: # 해당위치에서 나이트가 움직일 수 있는 좌표 파악
	cnt += 1
if (r + 2) < 9 and (c + 1) < 9:
	cnt += 1
if (r - 2) > 0 and (c - 1) > 0:
	cnt += 1
if (r - 2) > 0 and (c + 1) < 9:
	cnt += 1
if (r - 1) > 0 and (c + 2) < 9:
	cnt += 1
if (r + 1) < 9 and (c + 2) < 9:
	cnt += 1
if (r - 1) > 0 and (c - 2) > 0:
	cnt += 1
if (r + 1) > 0 and (c - 2) > 0:
	cnt += 1

print(cnt)


# N이 입력을 받으면 00시00분00초 ~ N시59분59초까지의 모든 시간 중 3이 하나라도 들어간 경우의 수를 구한다.


n = int(input())

cnt = 0

for i in range(n + 1): # 시간
	if i < 10:
		i = '0' + str(i) 
	for j in range(60): # 분
		if j < 10:
			j = '0' + str(j)
		for k in range(60): # 초
			if k < 10:
				k = '0' + str(k)
			time = str(i) + str(j) + str(k) # 전체 시간 
			for num in time: # 3이 들어간 시간을 카운트
				if (num == '3'):
					cnt += 1
					break
print(cnt)
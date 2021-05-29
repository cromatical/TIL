# 다양한 수로 이루어진 배열이 있을 떄 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙.
# 단, 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없는 것이 법칙.

# N, M ,K
n, m, k = map(int, input().split())
# N개 입력받기
lst = list(map(int, input().split()))

# 정렬후 뒤집어서 가장큰 수가 앞으로 나오게 하기.
lst.sort()
lst.reverse()

result = 0
cnt = k
while (m > 0): 
	if (cnt == 0): # K번을 더하고 난 뒤
		if (lst[0] != lst[1]): # 가장큰 수와 두번째 큰수가 다르면
			result += lst[1]
		else: # 가장큰 수와 두번째 큰 수가 같으면
			result += lst[0]
		cnt = k # K초기화
	else:	
		result += lst[0]
		cnt -= 1
	m -= 1

print(result)






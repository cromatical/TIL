n = int(input()) # 동전의 개수
coin_lst = []
coin_lst = list(map(int, input().split())) # 입력받을 코인

coin_lst.sort(reverse=True) # 큰수부터 내림차순 정렬 [9, 3, 2, 1, 1]

for i in range(1, 1000001): # 1 ~ 1,000,000원 까지
	money = i 
	for coin in coin_lst: # 코인리스트 
		if money >= coin: # 7 3 4 2 2 1 1 0
			money -= coin
		if money == 0:
			break
	if money != 0:
		break
print(i)
	

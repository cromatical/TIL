n = int(input())

# 큰 단위부터 확인
coin_lst = [500, 100, 50, 10]
cnt = 0

for i in coin_lst:
	cnt += n // i # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 
	n %= i

print(cnt)

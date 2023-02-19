# 랜선 개수 k, 그리고 필요한 개수 n이 입력된다.
# 편의를 위해 랜선을 자르거나 만들 때 손실되는 길이는 없다고 가정
# 기존의 k개의 랜선으로 n개의 랜선을 만들수 없는 경우는 없다.
# n개보다 많이 만드는 것도 n개를 만드는것에 포함
# 이때 만들수 있는 최대 랜선의 길이를 구하는 프로그램을 작성하라.

k, n = map(int, input().split())

lan_lst = []
for _ in range(k):
	lan_lst.append(int(input()))

start = 1 # total을 구할때 lan // mid 에서 나눠지므로 시작점을 1로 한다.
end = min(lan_lst) # 최소 n개는 만들어야 하므로 최소길이로 지정
total_lst = []

def solution(lan_lst, start, end, n): # 이진탐색
	if start > end:
		return None
	mid = (start + end) // 2 # 중간지점 파악
	total = sum([(lan // mid) for lan in lan_lst]) # 문제에서 요구하는 랜선의 개수
	print(total)
	if total < n: # n개 보다 작을 경우 
		return solution(lan_lst, start, mid - 1, n)
	else: # n개보다 같거나 큰 경우
		total_lst.append(mid)
		return solution(lan_lst, mid + 1, end, n)
	
# 재귀 x
# result = 0 # 최대 랜선길이 파악
# while (start <= end): # 반복문이 끝나는 조건
# 	total = 0
# 	mid = (start + end) // 2 # 중간지점 확인
# 	for lan in lan_lst: # 현재 길이로 나올수 있는 총 랜선 개수
# 		total += (lan // mid)
# 	if total < n: # n개 보다 작은 경우
# 		end = mid - 1
# 	else: # n개보다 같거나 큰 경우
# 		result = mid
# 		start = mid + 1

# print(result)


# 재귀 이용
solution(lan_lst, start, end, n)
print(total_lst)

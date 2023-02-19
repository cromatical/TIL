import sys
input = sys.stdin.readline

n, c = map(int, input().split())
lst = []
for _ in range(n):
	lst.append(int(input()))
lst.sort()

start = lst[1] - lst[0] # 거리가 가장 짧은 경우
end = lst[-1] - lst[0] # 거리가 가장 긴 경우
result = 0 # 최대간격이 저장될 변수

while start <= end:
	mid = (start + end) // 2
	count = 1 # 공유기 개수
	start_house = lst[0] # 공유기가 설치된 집
	
	for i in range(1, n): # 공유기 사이의 값을 넘겨줬을 때의 공유기의 개수 파악
		if mid <= lst[i] - start_house: # 현재 집에서 공유기를 설치하고자 할때 간격이 더 크기 떄문에 설치 가능
			count += 1
			start_house = lst[i]
	if count >= c: # 공유기 개수가 더 많은 경우
		start = mid + 1
		result = mid
	else: # 공유기 개수가 더 적은 경우
		end = mid - 1

print(result)
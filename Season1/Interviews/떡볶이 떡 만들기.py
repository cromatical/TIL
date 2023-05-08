# 손님이 왔을 때 요청한 총 길이가 M일 때 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값을 구하라

n, m = map(int, input().split())

lst = list(map(int, input().split()))
total_lst = []

start = 0
end = max(lst)

def solution(array, start, end, m):
	if start > end: # 이진탐색 끝나는 조건
		return None
	mid = (start + end) // 2 # 이진탐색 중간값
	total = sum([x - mid if x > mid else 0 for x in array]) # 문제에서 원하는 조건
	if total < m: # total이 떡볶이 길이보다 짧은 경우
		solution(array, start, mid - 1, m)
	else: # total이 떡볶이 길보다 같거나 긴 경우
		total_lst.append(mid) # 최대한 덜 잘랐을 때가 정답이므로 여기에서 기록!
		solution(array, mid + 1, end, m)

solution(lst, start, end, m)
print(max(total_lst))
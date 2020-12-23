# 여러개의 숫자 카드 중 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임
# 카드가 M x N 형태로 있다.
# 먼저 뽑고자 하는 행 선택, 그다음 가장 낮은 숫자를 뽑는다.

m, n = map(int, input().split())

max_num = 0
for i in range(m): # 행의 길이만큼 반복
	lst = list(map(int, input().split()))
	if max_num < min(lst): # n번째 행에서 규칙에 맞는 가장 작은 값을 찾아서 기존 값이랑 비교
		max_num = min(lst) 
print(max_num)


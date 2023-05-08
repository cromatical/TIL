# 정수 x가 주어질 때 정수 x에 사용할 수 있는 연산은 다음과 같다.
# 1. x가 5로 나누어 떨어지면 5로 나눈다.
# 2. x가 3로 나누어 떨어지면 3로 나눈다.
# 3. x가 2로 나누어 떨어지면 2로 나눈다.
# 4. x에서 1을 뺀다.
# 연산 4개를 적절히 사용해서 1을 만든다고 할 때 연산을 사용하는 횟수의 최솟값을 구하시오.

n = int(input())

d = [0] * 100 # 값 확인을 위한 dp테이블 생성
d[1] = 0 # 1은 초기값

for i in range(2, n + 1): # 2부터 n까지 확인
	lst = [] # 1~4번 연산을 통해 얻을수 있는 연산횟수를 저장할 리스트
	if i % 5 == 0: # 5로 나누어질 떄
		find_idx = i // 5
		lst.append(d[find_idx] + 1)
	if i % 3 == 0: # 3로 나누어질 떄
		find_idx = i // 3
		lst.append(d[find_idx] + 1)
	if i % 2 == 0: # 2로 나누어질 떄
		find_idx = i // 2
		lst.append(d[find_idx] + 1)
	find_idx = i - 1 # 1로 뺄때
	lst.append(d[find_idx] + 1)
	d[i] = min(lst) # 위 조건에 해당되는 1~4연산을 실행후 가장 작은 횟수를 선택

print(d)
print(d[n])
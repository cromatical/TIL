def solution(n, target, array):
	for i in range(n): # 각 원소를 하나씩 확인
		if array[i] == target: # 현재의 원소가 찾고자 하는 원소가 동일한 경우
			return i + 1 # 인덱스 위치를 반환
	return -1

print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하시오.")
input_data = input().split()
n = int(input_data[0]) # 원소 개수
target = input_data[1] # 찾고자 하는 문자열

print("앞서 적은 원소 개수만큼 문자열을 입력하시오. 구분은 띄어쓰기 한 칸으로 합니다.")
array = input().split()

# 순차탐색 수행 결과
print(solution(n, target, array))

def solution(s):
	result_lst = [] # 전체 결과 리스트를 담을 테이블

	for i in range(1, len(s) // 2 + 2): # 압축을 반 이상할 필요가 없기 때문에 다음과 같이 범위를 지정
		result = "" # 압축 결과를 넣을 빈 문자열
		j = 0 # 스타트 위치
		while j < len(s): # 문자열 전체를 한번 훑어 보기
			k = 0 # 같을 경우 위치 확인을 위한 변수 k
			cnt = 0 # 몇번 반복되었는지 확인을 위한 변수 cnt
			start = s[j:j + i] # start 변수
			# print("start :", start)
			while j + i <= len(s) and start == s[j + k:j + i + k]:
				cnt += 1
				k += i
			if cnt > 1: # cnt가 2개 이상일 경우 숫자 붙여주기
				j += k
				result += (str(cnt) + str(start))
			else:
				j += i
				result += str(start)	
		result_lst.append((i, len(result), result)) # (짜르는 단위, 총길이, 압축된 문자열)
		# print(result_lst)
	return min(result_lst, key=lambda x: x[1])[1] # 문자열의 길이가 가장작은 녀석을 들고온다.


s = ["aabbaccc",
	"ababcdcdababcdcd",
	"abcabcdede",
	"abcabcabcabcdededededede",
	"xababcdcdababcdcd"]

for i in range(len(s)):
	print(solution(s[i]))
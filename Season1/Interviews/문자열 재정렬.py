n = list(map(str, input())) # 입력
n.sort(reverse=True) # 내림차순으로 정렬 알파벳의 경우 A:65, '0':48

result = 0
while 1:
	try:
		result += int(n[-1]) # 숫자를 더해주는 부분
		n.pop() # 숫자 날라감
	except: # 알파벳의 경우 아스키 ord()로 바꾸지 않으면 에러가 발생함.
		break
n.sort() # 오름차순으로 정렬
n.append(str(result)) # 문자열로 변환
print("".join(i for i in n))
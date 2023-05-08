n = input() # 문자열 입력

result = int(n[0])
for i in n[1:]:
	if i == '0' or i == '1' or result == 0 or result == 1: # 만약 0이나 1이면 값을 더해준다.
		result += int(i)
	else: # 아닐경우 곱을 해준다.
		result *= int(i)
print(result)
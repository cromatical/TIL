
def fuc_1(p): # 균형잡힌 괄호인지 확인
	cnt = 0
	for i in range(len(p)):
		if p[i] == '(':
			cnt += 1
		else:
			cnt -= 1
		if cnt == 0:
			return i

def fuc_2(p): # 올바른 괄호인지 확인
	cnt = 0
	for i in p:
		if i == '(':
			cnt += 1
		else:
			cnt -= 1
		if cnt < 0:
			return 0
	return 1

def solution(p):
	answer = ""

	if len(p) == 0:
		return answer

	idx = fuc_1(p)
	u = p[:idx + 1]
	v = p[idx + 1:]

	if fuc_2(u):
		answer = u + solution(v)
	else:
		answer = '('
		answer += solution(v)
		answer += ')'

		u = list(u[1:-1])
		for i in range(len(u)):
			if u[i] == '(':
				u[i] = ')'
			else:
				u[i] = '('
		answer += "".join(u)
	return answer
	# 문자열 p를 u, v 두개로 분리

n = "(()())()"
print(solution(n))

 




	
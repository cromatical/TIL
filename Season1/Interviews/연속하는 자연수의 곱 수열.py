# 1. list의 n번째 인덱스를 리턴
# 2. 연속하는 자연수 두개 이상 곱해서 만듬

def solution1(n):
	num1 = 1
	num2 = 1
	lst = []
	
	while (n != i):
		if i == 0:
			lst.append(2)
		elif i % 4 == 0:
			num2 += 1
			ret = num2 * (num2+1) * (num2+2)
			if not ret in lst: 
				lst.append(ret)
		else:
			num1 += 1
			ret = num1 * (num1+1)
			if not ret in lst:
				lst.append(ret)
		i+=1
	return (lst)


def solution2(n):

	num1 = 1
	num2 = 1
	lst = []

	while (n != len(lst)):
		if len(lst) == 0:
			lst.append(2)
		else:
			ret1 = num1 * (num1+1)
			ret2 = num2 * (num2+1) * (num2+2)

			if ret1 > ret2:
				num2+=1
				if not ret2 in lst:
					lst.append(ret2)
			else:
				num1+=1
				if not ret1 in lst:	
					lst.append(ret1)
	return (lst)

n = int(input())

lst = solution2(n)
print(lst)
print(lst[-1])
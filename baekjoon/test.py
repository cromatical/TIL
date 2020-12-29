def solution(a, b):
	a, b = b, a
	return a, b

array = [1, 2]
a, b = solution(array[0], array[1])
print(a, b)
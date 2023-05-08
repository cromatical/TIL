array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

result = sorted(array) # sorted() 함수를 사용
print(result)


array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

array.sort() # sort() 함수를 사용
print(array) 


array = [('바나나', 2), ('사과', 5), ('당근', 3)]

def solution(data): # 정렬 라이브러리에서 key를 활용
	return data[1]

result = sorted(array, key=solution)
print(result)

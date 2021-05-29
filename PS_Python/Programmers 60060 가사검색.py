def left_solution(array, array2, start, end):
	if start > end:
		return None
	mid = (start + end) // 2

	target = array2[0]
	a, b = array2[1][0]
	if array[mid - 1][a:b] != target[a:b] and array[mid][a:b] == target[a:b] and len(array[mid]) == len(target):
		return mid
	elif array[mid] >= target:
		return left_solution(array, array2, start, mid - 1)
	else:
		return left_solution(array, array2, mid + 1, end)	

def right_solution(array, array2, start, end):
	if start > end:
		return None
	mid = (start + end) // 2
	target = array2[0]
	a, b = array2[1][0]
	if array[mid + 1][a:b] != target[a:b] and array[mid][a:b] == target[a:b] and len(array[mid]) == len(target):
		return mid
	elif array[mid] > target:
		return right_solution(array, array2, start, mid - 1)
	else:
		return right_solution(array, array2, mid + 1, end)	

def solution(words, queries):
	words.sort()
	wildcard_lst = []
	for querie in queries:
		wildcard = []
		i = 0
		while i < len(querie):
			if querie[i] != '?':
				start = i
				k = start
				while k < len(querie) and querie[k] != '?':
					k += 1
				end = k
				wildcard.append((start, end))
				i += k
			else:
				i += 1
		wildcard_lst.append((querie, wildcard))
	
	print(wildcard_lst)
	

	start = 0
	end = len(words) - 1
	result_lst = []
	for i in range(len(words)):
		a = left_solution(words, wildcard_lst[i], start, end)
		b = right_solution(words, wildcard_lst[i], start, end)
		print(a, b)


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
result = solution(words, queries)
print(result)
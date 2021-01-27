def solution2(numbers, target, total, i):
	print(numbers, target, total, i)
	if len(numbers) == i: # 재귀가 끝나는 조건이 필요한데... numbers[i]마지막일 때
		if total == target:
			return 1
		return 0
	b = numbers[i] # 인덱스
	return solution2(numbers, target, total + b, i + 1) + solution2(numbers, target, total - b, i + 1)

def solution(numbers, target):
	return solution2(numbers, target, numbers[0], 1) + solution2(numbers, target, -numbers[0], 1) 

n = list(map(int, input().split()))
t = int(input())
print(solution(n, t))
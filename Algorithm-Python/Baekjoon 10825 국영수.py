import sys
input = sys.stdin.readline

n = int(input()) # 학생수

student_lst = []
for _ in range(n):
	student_lst.append(input().split())
# for i in student_lst:
# 	print(i)

student_lst.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0])) # 국어, 영어, 수학, 이름 순으로
for i in student_lst:
	print(i[0])
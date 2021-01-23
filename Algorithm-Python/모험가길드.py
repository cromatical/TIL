n = int(input()) # 모험가 수
hero_lst = list(map(int, input().split())) # 모험가 리스트

hero_lst.sort(reverse=True)
# print(hero_lst)

i = 0
cnt = 0

while 1:
	a = hero_lst[i]	# [3, 2, 2, 2, 1]
	idx = 0
	j = i # 3번째 인덱스
	while a > 0: # 팀원 맞추기
		if j <= len(hero_lst): # 만약 j가 증가한 경우
			j += 1
			a -= 1
			idx += 1 # 3
		else: # j인덱스를 벗어날 때
			break
	i += idx # start를 idx만큼 증가
	if i == len(hero_lst): # 딱 팀이 맞을 경우
		cnt += 1
		break
	elif i > len(hero_lst): # 팀이 조금 부족한 경우
		break
	cnt += 1
print(cnt)
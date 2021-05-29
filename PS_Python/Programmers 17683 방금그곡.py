def solution(m, musicinfos):
	result_lst = [] # ((재생시간, 제목), ...)

	for music in musicinfos: # 노래들 확인
		# 12:00, 12:10, title, "ABCDAS"
		start_time, end_time, title, rhythm = map(str, music.split(','))
		
		new_rhythm = [] # ['A', 'B', 'C#']
		for i in rhythm: # 샾을 처리하기 위한 작업 (ABC#)
			if i == '#':
				new_rhythm.append(new_rhythm.pop() + '#')
			else:
				new_rhythm.append(i)

		new_start_time = list(map(int, start_time.split(':')))
		new_end_time = list(map(int, end_time.split(':')))

		hour = 0
		if new_start_time[1] < new_end_time[1]:
			hour = abs(new_start_time[0] - new_end_time[0]) 
		length = (hour * 60) + abs(new_start_time[1] - new_end_time[1]) # 11:50 ~ 12:10

		result = [] # 총 시간만큼 들어가는 리듬
		for i in range(length):
			i %= len(new_rhythm)
			result.append(new_rhythm[i])

		new_m = [] # 기억하고 있는 리듬
		for i in m:
			if i == '#':
				new_m.append(new_m.pop() + '#')
			else:
				new_m.append(i)

		for i in range(len(result)): # 기억하고 있는 리듬이 시간동안 반복된 리듬속에 존재하는지 확인
			j = 0
			start = i
			if result[start] == new_m[j]:
				while start < len(result) and j < len(new_m) and result[start] == new_m[j]:
					start += 1
					j += 1
				if j == len(new_m): # 찾고자하는 문자열이 존재하는 경우 반복문 종료
					result_lst.append((len(result), title))
					break

		if i == len(result)	- 1:
			result_lst.append((0, "(None)"))

	return max(result_lst)[1]

# m = "ABCDEFG"
# musicinfos = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]

# m = "CC#BCC#BCC#BCC#B"
# musicinfos = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]

# m = "ABC"
# musicinfos = ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]
# print(solution(m, musicinfos))

# print(solution("A#", ["13:00,13:02,HAPPY,B#A#"])) # A#, [13:00,13:02,HAPPY,B#A#], HAPPY
# print(solution("CDEFGAC", ["12:00,12:06,HELLO,CDEFGA"])) # CDEFGAC, [12:00,12:06,HELLO,CDEFGA], (None)
# print(solution("CCB", ["03:00,03:10,FOO,CCB#CCB", "04:00,04:08,BAR,ABC"])) # CCB, [03:00,03:10,FOO,CCB#CCB, 04:00,04:08,BAR,ABC], FOO
# n= int(input())

# activity_lst = []
# for i in range(n):
    # lst = list(map(int, input().split()))
    # activity_lst.append(lst)

activity_lst = [
    [2, 4], [2, 7], [1, 4], [5, 9], [3, 5], [8, 10], [2, 4], [6, 9], [1, 7], [8, 9], [9, 10]
]

activity_lst.sort()  # 탐욕법으로 선택시 가장 빨리 끝나는 강의 선택하기 위한 정렬

result = []
first_activity = activity_lst[0]  # 첫번째 가장 빨리 끝나는 강의 선택
count = 0

next_activity = []  # 첫번째 강의 이후 선택할 강의 초기화

for activity_time in activity_lst:
    if len(result) == 0:  # 아직 강의를 선택하지 않았을 때 가장 빨리 끝나는 강의 선택
        result.append(activity_time)
        count += 1
    
    start_time, end_time = activity_time[0], activity_time[1]
    
    if count == 1:  # 첫번째 강의 이후 다음 가장 빨리 끝나는 강의를 선택
        first_activity_start_time, first_activity_end_time = first_activity[0], first_activity[1]
        
        if first_activity_end_time <= start_time:
            next_activity = activity_time
            result.append(next_activity)
            count += 1
    else:  # 이후 강의 가장 빨리 끝나는 강의를 선택
        next_activity_start_time, next_activity_end_time = next_activity[0], next_activity[1]
        
        if next_activity_end_time <= start_time:
            next_activity = activity_time
            result.append(next_activity)
            count += 1

print(f"Activity choice lst: {result}")
print(f"Activity best lst: {count}")

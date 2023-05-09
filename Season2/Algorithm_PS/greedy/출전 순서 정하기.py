'''
출전 순서 정하기
    - 어떻게 매칭 시켜야 b팀의 승수를 최대로 할 수 있는가?
'''

n = 6
a_team = [3000, 2700, 2800, 2200, 2500, 1900]
b_team = [2800, 2750, 2995, 1800, 2600, 2000]

a_team.sort()
b_team.sort()

arrange_a_team = []
arrange_b_team = []

count = 0

for _ in range(n):
    a_team_member = a_team[-1]  # a팀 첫번째 선수
    b_team_member = b_team[-1]  # b팀 첫번째 선수
    
    if a_team_member > b_team_member:  # a팀 선수가 b선수보다 점수가 높을 때
        a_member = a_team.pop()
        arrange_a_team.append(a_member)
        
        b_member = b_team.pop(0)  # b팀에서 가장 점수 낮은 사람 매칭
        arrange_b_team.append(b_member)
    
    else:  # 그외 경우엔 그대로 매칭
        a_member = a_team.pop()
        arrange_a_team.append(a_member)
        
        b_member = b_team.pop()
        arrange_b_team.append(b_member)
        count += 1

print("Rearrange member list")
print(arrange_a_team)
print(arrange_b_team)
print(count)
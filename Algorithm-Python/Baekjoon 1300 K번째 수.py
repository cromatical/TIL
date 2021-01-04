# ex) 8이하의 수를 mid로 잡을 경우
# 1 2 3 4	==> 8배수로 8이 존재할 위치가 8이지만 N이 4이므로 min을 통해 최대 4개만 가지도록 함
# 2 4 6 8	==> 4
# 3 6 9 12	==> 2.xx
# 4 8 12 16  ==> 2
# 다음을 통해 mid 8이 존재할 위치 모든 인덱스를 다 더해서 8이 있을 인덱스를 파악.

import sys
input=sys.stdin.readline

N = int(input())
K = int(input())
start, end = 1, K # 0~N*N번째 수를 나열

while start <= end:
    mid = (start + end) // 2 # 기준값 설정
    
    temp = 0
    for i in range(1, N+1):
        temp += min(mid//i, N) # mid 이하의 i의 배수 or 최대 N개가 되도록
							   
    if temp >= K: #이분탐색 실행
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer)
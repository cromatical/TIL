import sys
input = sys.stdin.readline

n = int(input())
house_lst = list(map(int, input().split()))
house_lst.sort() # 정렬
print(house_lst[len(house_lst)//2-1]) # 중간값의 위치가 가장 작은 값을 가지고 있다.
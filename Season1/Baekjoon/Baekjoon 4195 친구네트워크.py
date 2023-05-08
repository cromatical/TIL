import sys
sys.setrecursionlimit(500000)
input = sys.stdin.readline

n = int(input()) # 테스트케이스 수

def find_parent(friend_network, x):
	if x != friend_network[x]:
		friend_network[x] = find_parent(friend_network, friend_network[x])
	return friend_network[x]

def union_parent(friend_network, a, b):
	a = find_parent(friend_network, a)
	b = find_parent(friend_network, b)
	if friend_num[a] < friend_num[b]:
		# {"Fred" : 0, "Barney" : 1 ... }
		friend_network[b] = a
	else:
		friend_network[a] = b

for _ in range(n):
	f = int(input()) # 친구 관계의 수 
	friend_network = {}
	friend_num = {}
	i = 0
	for _ in range(f):
		a, b = input().split() # 두 친구관계 입력
		if not a in friend_network:
			friend_network[a] = a # 자기자신을 부모로
			friend_num[a] = i
			i += 1
		if not b in friend_network:
			friend_network[b] = b # 자기자신을 부모로
			friend_num[b] = i
			i += 1
		
		union_parent(friend_network, a, b)
		check = find_parent(friend_network, a) # 친구놈의 부모파악

		cnt = 0
		for k, v in friend_network.items(): # 해당 딕셔너리에서 key, value 가지고옴
			if check == find_parent(friend_network, k): # 친구놈의 최상위 포식자 확인
				cnt += 1
		print(cnt)

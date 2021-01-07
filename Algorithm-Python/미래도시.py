INF = int(1e9) # 무한의 값 10억 세팅

n, e = map(int, input().split()) # 노드, 간선의 개수
graph = [[INF] * (n + 1) for _ in range(n + 1)] # 노드들 간의 정보 저장

for _ in range(e): # 간선 거리 입력
    a, b = map(int, input().split())
    graph[a][b] = 1 # 회사간의 거리는 1
    graph[b][a] = 1

x, k = map(int, input().split()) # k번째회사를 들렸다가 x회사로 감 입력!

for a in range(1, n + 1): # 자기자신 초기화
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0


for c in range(1, n + 1): # 플로이드 워셜 알고리즘 수행
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][c] + graph[c][b])

for a in range(1, n + 1): # 전체 테이블 출력
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print("INF")
        else:
            print(graph[a][b], end=" ")
    print("")


if graph[1][k] + graph[k][x] == INF: # 만약 x회사에 도달할수 없다면    
    print("-1")
else:
    print(graph[1][k] + graph[k][x])

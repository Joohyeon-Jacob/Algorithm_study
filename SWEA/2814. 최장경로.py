import sys
sys.stdin = open('sample_input_최장경로.txt', 'r')

def dfs(idx, cnt):
    global result

    # result 업데이트
    if result < cnt:
        result = cnt

    for i in range(1, N+1):
        # 방문하지 않았고 & 경로에 포함될 경우
        if visited[i] == 0 and adj[idx][i] == 1:
            visited[i] = 1
            dfs(i, cnt+1)
            visited[i] = 0


T = int(input())

for tc in range(1, T+1):
    # N : 정점 / M : 간선
    N, M = map(int, input().split())

    adj = [[0]*(N+1) for _ in range(N+1)]

    visited = [0]*(N+1)

    for _ in range(M):
        # 간선 정보
        a, b = map(int, input().split())

        # 무방향 그래프
        adj[a][b] = 1
        adj[b][a] = 1

    # 경로 길이(경로에 등장하는 정점 개수)
    result = 0

    # dfs
    for i in range(1, N+1):
        visited[i] = 1
        dfs(i, 1) # 첫 번째 정점부터 cnt에 포함
        visited[i] = 0

    print(f'#{tc} {result}')
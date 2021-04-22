import sys
sys.stdin = open('sample_input_그룹 나누기.txt', 'r')

def dfs(idx):

    for i in range(1, N+1):
        if visited[i] == 0 and adj[idx][i] == 1:
            visited[i] = 1
            dfs(i)

T = int(input())

for tc in range(1, T+1):
    # N : 출석번호 수 / M : 같은 조 신청서 수
    N, M = map(int, input().split())

    request = list(map(int, input().split()))

    # 인접 행렬
    adj = [[0]*(N+1) for _ in range(N+1)]

    visited = [0]*(N+1)

    for i in range(M):
        n1 = request[i*2]
        n2 = request[i*2+1]

        # 무방향
        adj[n1][n2] = 1
        adj[n2][n1] = 1

    # 신청서 개수
    result = 0

    # dfs
    for i in range(1, N+1):
        if visited[i] == 0:
            dfs(i)
            result += 1

    print(f'#{tc} {result}')
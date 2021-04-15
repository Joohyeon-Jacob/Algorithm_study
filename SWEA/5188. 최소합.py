import sys
sys.stdin = open('sample_input_최소합.txt', 'r')

dx = [0, 1]
dy = [1, 0]

# 탐색

def dfs(x, y, min_total):
    global result

    min_total += arr[x][y]

    # min_total 업데이트 안하는 경우
    if min_total > result:
        return

    if x == N-1 and y == N-1:
        if min_total < result:
            result = min_total
        return

    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx <= N-1 and ny <= N-1:
            dfs(nx, ny, min_total)

# 테스트 케이스
T = int(input())

for tc in range(1, T+1):
    # 배열 크기 : N*N
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    # 탐색 경로 값
    result = 1000

    dfs(0, 0, 0)

    print('#{} {}'.format(tc, result))
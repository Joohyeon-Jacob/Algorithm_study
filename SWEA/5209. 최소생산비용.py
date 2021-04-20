import sys
sys.stdin = open('sample_input_최소생산비용.txt', 'r')

def dfs(idx, total):
    global result

    # 마지막 열 도달
    if idx == N:
        # total 업데이트(더 작은 값으로)
        if result > total:
            result = total

    # total 값이 더 크면 업데이트 안 함
    if result < total:
        return

    # 각 행 순회
    for i in range(N):
        # 방문하지 않은 곳
        if visited[i] == 0:
            # 방문 표시
            visited[i] = 1
            # 시작 지점 이동
            dfs(idx+1, total+arr[idx][i])
            # 되돌리기
            visited[i] = 0

T = int(input())

for tc in range(1, T+1):
    # 제품 수
    N = int(input())

    # 공장별 생산비용
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 방문 표시
    visited = [0]*N

    # 최소 비용
    result = 2000

    dfs(0, 0)

    print(f'#{tc} {result}')
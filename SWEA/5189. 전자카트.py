import sys
sys.stdin = open('sample_input_전자카트.txt', 'r')

def recursion_trace(x, cnt, total): # x : idx
    global min_cost

    # 최소 비용 업데이트할 필요가 없음
    if min_cost < total:
        return

    # 지역 순회 완료
    if cnt == N-1:
        total += arr[x][0]
        # 최소 비용 갱신
        if min_cost > total:
            min_cost = total
            return

    for i in range(1, N):
        if visited[i] == 0 and arr[x][i]:
            visited[i] = 1
            total += arr[x][i]
            cnt += 1
            recursion_trace(i, cnt, total)

            visited[i] = 0
            total -= arr[x][i]
            cnt -= 1


# 테스트 케이스
T = int(input())

for tc in range(1, T+1):
    # 배열 크기 : N*N
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    # 방문한 지점 표시
    visited = [0]*N

    # 최소 비용
    min_cost = 1000 # 100 * 10

    recursion_trace(0, 0, 0)

    print(f'#{tc} {min_cost}')
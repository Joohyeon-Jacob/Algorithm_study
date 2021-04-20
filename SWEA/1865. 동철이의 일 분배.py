import sys
# import time
# start = time.time()
sys.stdin = open('input_동철이의 일 분배.txt', 'r')

def backtrack(idx, percent):
    global result
    # result 업데이트(더 큰 확률로)
    if result < percent:
        if idx == N:
            result = percent
        else:
            for i in range(N):
                if visited[i] == 0:
                    visited[i] = 1
                    # idx 이동 & percent 업데이트
                    backtrack(idx+1, percent*(success_rate[idx][i])/100)
                    visited[i] = 0

    # dfs 형태로 풀었을때는 시간 초과.. 백트래킹과 차이가 발생하는 이유가 아직 명확하게
    # 이해가 되지를 않는다.

    # if result > percent:
    #     return

    # for i in range(N):
    #     if visited[i] == 0:
    #         visited[i] = 1
    #         backtrack(idx + 1, percent * (success_rate[idx][i]) / 100)
    #         visited[i] = 0

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    # N명의 직원 각각의 성공 확률 리스트
    success_rate = [list(map(int, input().split())) for _ in range(N)]

    # 가장 높은 확률
    result = 0

    # 방문 배열
    visited = [0]*N

    # 백트래킹
    backtrack(0, 100)

    print(f'#{tc} {result:.6f}')

# print(time.time()-start)
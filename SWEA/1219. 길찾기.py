# 일방통행 -> 방향성 그래프

import sys
sys.stdin = open('input_길찾기.txt','r')

def dfs(n): # n : 현재 위치
    # print(n, end=' ') # 현재 node 출력
    order_list.append(n)
    visited[n] = 1 # 방문 표시
    for i in range(100):
        if adj[n][i] == 1 and visited[i] == 0:
            dfs(i)

# 테스트 케이스
T = 10

for tc in range(1, T+1):
    # start -> end 방향 노드 흐름 담을 리스트
    order_list = []
    # 노드 존재 여부 초기값
    result = 0
    num, E = map(int, input().split())
    Edge = list(map(int, input().split()))
    visited = [0]*100
    adj = [[0] * 100 for _ in range(100)]

    for i in range(E):
        n1, n2 = Edge[i * 2], Edge[i * 2 + 1]
        adj[n1][n2] = 1

    dfs(0)

    for num in order_list:
        # 노드 존재 여부 체크
        if num == 99:
            # result 업데이트
            result = 1
            break

    print('#{} {}'.format(tc, result))
# 방향성 그래프

import sys
sys.stdin = open('sample_input_그래프경로.txt','r')

def dfs(n): # n : 현재 위치
    # print(n, end=' ') # 현재 node 출력
    order_list.append(n)
    visited[n] = 1 # 방문 표시
    for i in range(1, V+1):
        if Edge[n][i] == 1 and visited[i] == 0:
            dfs(i)

# 테스트 케이스
T = int(input())

for tc in range(1, T+1):
    # start -> end 방향 노드 흐름 담을 리스트
    order_list = []
    # 노드 존재 여부 초기값
    result = 0
    V, E = map(int, input().split())
    Edge = [[0]*(V+1) for _ in range(V+1)]
    visited = [0]*(V+1)
    for _ in range(E):
        i, j = map(int, input().split())
        Edge[i][j] = 1 # 방향성 그래프이기 때문에 여기만 1 업데이트

    # start -> end 노드로 가는 경로 존재하는지 확인
    start, end = map(int, input().split())
    dfs(start)

    for num in order_list:
        # 노드 존재 여부 체크
        if num == end:
            # result 업데이트
            result = 1
            break

    print('#{} {}'.format(tc, result))

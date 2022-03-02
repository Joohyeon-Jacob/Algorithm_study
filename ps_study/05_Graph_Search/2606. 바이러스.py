
import sys

def dfs(k):
    """k : 시작점"""
    global answer

    answer += 1
    visited[k] = True

    for i in range(N+1):
        if not visited[i] and graph[k][i] == 1:
            dfs(i)


if __name__ == "__main__":
    # 컴퓨터 수
    N = int(input())
    # 연결된 컴퓨터 쌍의 개수
    M = int(input())

    graph = [[0] * (N+1) for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        graph[a][b] = 1
        graph[b][a] = 1

    visited = [False] * (N+1)
    answer = -1

    dfs(1)
    print(answer)


"""https://resilient-923.tistory.com/296"""

import sys

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y, cnt):
    global Max
    if Max < cnt:
        Max = cnt

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 문자열 처리하니까 시간초과가 난다 알파벳개수만 큼 리스트 만들어서
        if 0 <= nx < r and 0 <= ny < c and visited[graph[nx][ny]] == 0:
            visited[graph[nx][ny]] = 1
            dfs(nx, ny, cnt + 1)
            visited[graph[nx][ny]] = 0

if __name__ == "__main__":
    input = sys.stdin.readline

    r, c = map(int, input().split())
    graph = [list(map(lambda a: ord(a) - 65, input())) for _ in range(r)]
    visited = [0] * 26

    Max = 1

    visited[graph[0][0]] = 1
    dfs(0, 0, Max)

    print(Max)
import sys
from collections import deque

dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs():
    global dist, table

    q = deque()
    q.append((0, 0, 1))
    dist[0][0][1] = 1

    while len(q) > 0:
        y, x, block = q.popleft()

        if y == (N - 1) and x == (M - 1):
            return dist[y][x][block]

        for dx1, dy1 in dxy:
            dy = y + dy1
            dx = x + dx1
            if 0 <= dy < N and 0 <= dx < M:
                if table[dy][dx] == 1 and block == 1:
                    dist[dy][dx][block - 1] = dist[y][x][block] + 1
                    q.append((dy, dx, block - 1))
                elif table[dy][dx] == 0 and dist[dy][dx][block] == 0:
                    dist[dy][dx][block] = dist[y][x][block] + 1
                    q.append((dy, dx, block))
    return -1


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    table = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
    dist = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    answer = bfs()

    print(answer)


import sys
from collections import deque

dxy = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def solve():
    """인접한 토마토가 익은 토마토인지 체크하므로 bfs 적용"""
    ans = 0
    q = deque()
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                q.append((i, j))
                check[i][j] = True

    while len(q):
        q_size = len(q)
        for i in range(q_size):
            current = q.popleft()

            for tp in dxy:
                np = (current[0] + tp[0], current[1] + tp[1])
                if inside_board(np) and board[np[0]][np[1]] == 0 \
                        and check[np[0]][np[1]] == False:
                    q.append(np)
                    check[np[0]][np[1]] = True
                    board[np[0]][np[1]] = 1

        ans += 1
        # print(ans)

    if is_all_ripen():
        return ans - 1
    else:
        return -1


def is_all_ripen():
    """아직 안 익은 토마토가 있는지 체크"""
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                return False
    return True


def inside_board(p):
    return 0 <= p[0] < N and 0 <= p[1] < M

if __name__ == "__main__":
    M, N = map(int, sys.stdin.readline().split())
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    check = [[False] * M for _ in range(N)]

    result = solve()
    print(result)

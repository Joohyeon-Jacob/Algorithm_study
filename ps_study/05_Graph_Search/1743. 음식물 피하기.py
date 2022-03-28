import sys
sys.setrecursionlimit(1000000)


def solve():
    ans = 0

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if table[i][j] == 1:
                ans = max(ans, dfs(i, j, 1))

    return ans


def dfs(i, j, cnt):
    table[i][j] = 0
    if i - 1 > 0 and table[i - 1][j] == 1:
        cnt += dfs(i - 1, j, 1)
    if j - 1 > 0 and table[i][j - 1] == 1:
        cnt += dfs(i, j - 1, 1)
    if i + 1 <= N and table[i + 1][j] == 1:
        cnt += dfs(i + 1, j, 1)
    if j + 1 <= M and table[i][j + 1] == 1:
        cnt += dfs(i, j + 1, 1)

    return cnt


if __name__ == "__main__":
    N, M, K = map(int, sys.stdin.readline().split())

    table = [[0] * (M + 1) for _ in range(N + 1)]
    check = [[False] * (M + 1) for _ in range(N + 1)]

    for i in range(K):
        a, b = map(int, sys.stdin.readline().split())
        table[a][b] = 1

    answer = solve()
    print(answer)
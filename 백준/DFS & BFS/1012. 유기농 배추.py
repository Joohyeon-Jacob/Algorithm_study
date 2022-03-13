
import sys
sys.setrecursionlimit(10**6)

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def dfs(x, y):
    # 배추 심어져 있는 지 체크
    if arr[x][y] == 1:
        arr[x][y] = 0
        for i in range(4):
            if move_possible(x+dx[i], y+dy[i]):
                dfs(x+dx[i], y+dy[i])
        return True
    return False


def move_possible(x, y):
    """이동 가능한 경로인지 체크"""
    if (x >= 0 and x < M) and (y >= 0 and y < N):
        return True
    return False

if __name__ == "__main__":
    # 테스트 케이스 개수
    T = int(input())
    for _ in range(T):
        # N : 가로 길이, M : 세로 길이, K : 배추 위치 개수
        N, M, K = map(int, sys.stdin.readline().split())
        # 배추밭
        arr = [[0] * N for _ in range(M)]
        for _ in range(K):
            b, a = map(int, sys.stdin.readline().split())
            arr[a][b] = 1
        # 필요한 지렁이 수
        worm_cnt = 0
        for i in range(M):
            for j in range(N):
                if dfs(i, j):
                    worm_cnt += 1
        print(worm_cnt)


import collections

def move_possible(x, y):
    if (x >= 0 and x < N) and (y >= 0 and y < M) and arr[x][y] == 1:
        return True
    return False

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


if __name__ == "__main__":
    N, M = map(int, input().split()) # target : (N-1, M-1)
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input())))

    Q = collections.deque([(0, 0)])
    while Q:
        x, y = Q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if move_possible(nx, ny):
                if arr[nx][ny] == 1:
                    arr[nx][ny] = arr[x][y] + 1
                    Q.append((nx, ny))

    print(arr[N-1][M-1])
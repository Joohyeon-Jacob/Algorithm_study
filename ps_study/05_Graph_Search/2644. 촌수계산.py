
import sys
from collections import deque

def bfs(start, end):
    count = 0
    q = deque()
    q.append(start)
    check[start] = True

    while len(q):
        q_size = len(q)
        for i in range(q_size):
            current = q.popleft()

            if current == end:
                return count

            for j in range(1, n+1):
                if not check[j] and table[current][j]:
                    check[j] = True
                    q.append(j)
        count += 1

    # 촌수 관계 없을 경우
    return -1


if __name__ == "__main__":
    # n : 전체 사람 수
    n = int(input())
    # 촌수 계산 대상 두 사람 번호
    start, end = map(int, sys.stdin.readline().split())
    # 부모 - 자식 관계 수
    m = int(input())

    check = [False] * (n+1)
    table = [[False] * (n+1) for _ in range(n+1)]

    for i in range(m):
        x, y = map(int, sys.stdin.readline().split())
        table[x][y] = True
        table[y][x] = True

    answer = bfs(start, end)
    print(answer)

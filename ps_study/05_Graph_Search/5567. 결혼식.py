
import sys
from collections import deque

def bfs(start):
    q = deque()
    q.append(start)
    check[start] = True

    # 상근이의 친구의 친구(depth=2)까지만 탐색
    depth = 0
    answer = 0

    while len(q):
        q_size = len(q)
        if depth == 2:
            return answer

        for i in range(q_size):
            current = q.popleft()

            for j in range(1, N+1):
                if not check[j] and connections[current][j]:
                    check[j] = True
                    q.append(j)
                    answer += 1
        depth += 1
    return 0

if __name__ == "__main__":
    # 상근이 동기의 수
    N = int(input())
    M = int(input())

    connections = [[False] * (N+1) for _ in range(N+1)]

    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        connections[a][b] = True
        connections[b][a] = True

    check = [False] * (N+1)
    result = bfs(1)
    print(result)

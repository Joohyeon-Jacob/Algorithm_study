'''
출처 : https://velog.io/@hamfan524/%EB%B0%B1%EC%A4%80-1260%EB%B2%88-Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC
'''

from collections import deque
import sys

def bfs(v):
    q = deque()
    q.append(v)
    visit_list_bfs[v] = 1
    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in range(1, N+1):
            if visit_list_bfs[i] == 0 and graph[v][i] == 1:
                q.append(i)
                visit_list_bfs[i] = 1

def dfs(v):
    visit_list_dfs[v] = 1
    print(v, end=' ')
    for i in range(1, N+1):
        if visit_list_dfs[i] == 0 and graph[v][i] == 1:
            dfs(i)

N, M, V = list(map(int, sys.stdin.readline().split()))

graph = [[0]*(N+1) for _ in range(N+1)]

visit_list_bfs = [0]*(N+1)
visit_list_dfs = [0]*(N+1)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1


if __name__ == "__main__":
    dfs(V)
    print()
    bfs(V)
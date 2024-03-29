import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
graph = [[] for _ in range(n+1)]

def dfs(x, weight):
    for i in graph[x]:
        a, b = i
        if distance[a] == -1:
            distance[a] = weight+b
            dfs(a, weight+b)

# 트리
for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

# 1번 노드에서 가장 먼 노드 찾기
distance = [-1] * (n+1)
distance[1] = 0
dfs(1, 0)

# 위에서 찾은 노드에서 가장 먼 노드 찾기
start = distance.index(max(distance))
distance = [-1] * (n+1)
distance[start] = 0
dfs(start, 0)

print(max(distance))
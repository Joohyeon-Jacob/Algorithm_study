
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
N = int(input())

# 트리
tree = [[] for _ in range(N+1)]

# 부모 노드
parents = [0 for _ in range(N+1)]

# 트리 구조
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(start, tree, parents):
    # 연결된 노드부터 parents[i]의 부모가 없으면 부모 설정 해주고, dfs 돌린다
    for i in tree[start]:
        if parents[i] == 0:
            parents[i] = start
            dfs(i, tree, parents)

dfs(1, tree, parents)

for i in range(2, N+1):
    print(parents[i])
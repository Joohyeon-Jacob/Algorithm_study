
def dfs(num, sum):
    global visited
    visited[sum] = True

    if num == N:
        return

    # 해당 num 더할 경우
    dfs(num+1, sum+S[num])

    # 해당 num 더하지 않을 경우
    dfs(num+1, sum)


if __name__ == "__main__":
    N = int(input())
    S = list(map(int, input().split()))

    visited = [False] * 100000 * N

    dfs(0, 0)

    length = len(visited)

    for i in range(1, length):
        if not visited[i]:
            print(i)
            break

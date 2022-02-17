
from itertools import permutations

def perm(depth):
    if depth == N:
        for number in output:
            print(number, end=' ')
        print()
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            output[depth] = arr[i]
            perm(depth+1)
            visited[i] = False


if __name__ == "__main__":
    N = int(input())
    arr = [num for num in range(1, N+1)]

    '''
    파이썬 라이브러리 사용
    for element in permutations(arr, N):
        for num in element:
            print(num, end=' ')
        print()
    '''

    # DFS
    visited = [False] * N
    output = [0] * N
    perm(0)

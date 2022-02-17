
# DFS 이용
def perm(depth, reverse):
    global flag

    if depth == N+1:
        print(str(''.join(map(str, output))))
        flag = True
        return

    for k in range(10):
        if reverse:
            i = 9 - k
        else:
            i = k

        if not visited[i] and not flag:
            if depth == 0 or check(signs[depth-1], output[depth-1], i):
                visited[i] = True
                output[depth] = i
                perm(depth+1, reverse)
                visited[i] = False


def check(sign, val1, val2):
    if sign == '<' and val1 < val2:
        return True
    if sign == '>' and val1 > val2:
        return True

    return False


if __name__ == "__main__":
    # 부등호 개수
    N = int(input())
    signs = input().split()

    visited = [False] * 10
    output = [0] * (N+1)

    flag = False
    perm(0, True)

    flag = False
    perm(0, False)

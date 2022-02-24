
if __name__ == "__main__":
    N = int(input())
    A_list = list(map(int, input().split()))
    B_list = list(map(int, input().split()))

    A_list.sort()
    B_list.sort(reverse=True)

    # S의 최소값
    S_result = 0

    for i in range(N):
        S_result += A_list[i] * B_list[i]

    print(S_result)

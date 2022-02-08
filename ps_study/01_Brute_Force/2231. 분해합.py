
import sys

def split_sum(k):
    target_num = k

    while k:
        # 나머지를 더하고, 10으로 나눈 수의 나머지를 더하고..
        target_num += k % 10
        k = k // 10

    return target_num

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    M = 0

    for i in range(N):
        if N == split_sum(i):
            # 분해합 찾음
            M = i
            break

    print(M)
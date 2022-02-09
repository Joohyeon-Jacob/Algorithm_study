
import sys

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())

    color_info_list = []

    for _ in range(N):
        color_info_list.append(input())

    answer = 8 * 8

    for i in range(N-7):
        for j in range(M-7):
            BW, WB = 0, 0
            for ki in range(8):
                for kj in range(8):
                    if (ki+kj) % 2 == 0 and color_info_list[i+ki][j+kj] != 'B':
                        BW += 1
                    elif (ki+kj) % 2 == 1 and color_info_list[i+ki][j+kj] != 'W':
                        BW += 1
                    WB = 64 - BW
            answer = min(answer, BW, WB)

    print(answer)
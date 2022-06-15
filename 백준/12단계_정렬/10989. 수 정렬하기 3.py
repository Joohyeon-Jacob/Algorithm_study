
import sys

N = int(sys.stdin.readline())
num_list = [0] * 10001

for _ in range(N):
    num = int(sys.stdin.readline())
    num_list[num] += 1

for idx, value in enumerate(num_list):
    if value != 0:
        for _ in range(value):
            print(idx)

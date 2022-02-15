
import sys
from itertools import combinations

# 원소 개수 / 원소 합 기준
N, S = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))
length = len(arr)

# 부분집합 모음
subsets = []
for i in range(length+1):
    subsets = subsets + list(combinations(arr, i))

# 부분집합 원소 합 0인 경우의 개수
subset_sum_zero = 0

# 공집합 제외
subsets.pop(0)

for subset in subsets:
    if sum(subset) == S:
        subset_sum_zero += 1

print(subset_sum_zero)


# 각 순열마다 이웃한 수의 차의 합을 계산 --> 최대값 구하기

from itertools import permutations

if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))

    max_result = 0

    for element in permutations(arr, N):
        sum_element = 0
        for i in range(1, N):
            sum_element += abs(element[i] - element[i-1])
            max_result = max(max_result, sum_element)

    print(max_result)
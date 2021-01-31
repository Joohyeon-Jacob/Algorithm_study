# 백준 10871번 : X보다 작은 수

import sys

import time
start = time.time()  # 시작 시간 저장

# https://tekiter.tistory.com/3 숫자 여러 개 input 할때 참고할 문서

n, x = map(int, input().split())

# nums = [int(input()) for _ in range(n)] -> 이 코드는 원하는 결과 안 나와서 고민함

numbers = [int(n) for n in input().split()]
# print(numbers)

for num in numbers:
    if num < x:
        print(num, end=' ')

# print()
print("time :", time.time() - start)
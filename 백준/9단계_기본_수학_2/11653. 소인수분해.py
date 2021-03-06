# 소인수분해할 정수
N = int(input())

# 소인수 초기값
k = 2

# 1보다 크면 소인수분해 진행 가능
while N > 1:
    if N % k == 0:
        print(k)
        N //= k
    # 나누어 떨어지지 않으면, 소인수 1 증가
    else:
        k += 1
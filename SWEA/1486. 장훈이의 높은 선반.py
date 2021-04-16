import sys
sys.stdin = open('input_장훈이의 높은 선반.txt', 'r')

# 테스트 케이스
T = int(input())

for tc in range(1, T+1):
    # N : 점원 수 / B : 선반 높이
    N, B = map(int, input().split())

    # 점원들의 키
    height = list(map(int, input().split()))

    n = len(height)

    # B(선반 높이) 이상인 탑의 높이 -> 탑과 선반 높이와의 차이 중 최소값
    result = sum(height)

    for i in range(1 << n):
        # 부분집합의 원소들의 합
        value = 0
        for j in range(n):
            if i & (1 << j):
                # print(height[j], end=' ')
                value += height[j]

        # 탑의 높이(부분집합 원소의 합) 이 탑의 높이 이상 / 탑의 높이와의 차이 최소값 업데이트
        if value >= B and result > value - B:
            result = value - B

    print(f'#{tc} {result}')
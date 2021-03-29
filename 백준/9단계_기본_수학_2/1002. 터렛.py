import math

# 테스트 케이스
T = int(input())

for tc in range(1, T+1):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    d = math.sqrt((x1-x2)**2 + (y1-y2)**2)

    # 두 원이 서로 만나지 않을때(바깥에서 & 한 원이 다른 원 안에 있을 경우 & 반지름의 길이가 다른 동심원)
    if d > r1+r2 or d < abs(r1-r2) or (d == 0 and r1 != r2):
        print(0)

    # 두 원이 접할 경우(바깥 또는 한 원이 다른 원 안에서 접할 경우)
    elif d == r1+r2 or d == abs(r1-r2):
        print(1)

    # 두 원이 서로 다른 두 점에서 만날 경우
    elif d < r1+r2 and d > abs(r1-r2):
        print(2)

    # 두 원이 일치할 경우
    elif d == 0 and r1 == r2:
        print(-1)
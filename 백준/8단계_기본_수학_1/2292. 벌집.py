import time
start = time.time()

# 특정 숫자가 지나는 방의 최소 개수(1번방에서 출발)

# 특정 숫자
T = int(input())

# 방 이동하는 횟수
n = 1

if T == 1:
    print(1)

else:
    while True:
        # 1 -> 7(1+6) -> 19(1+6+12) -> 37(1+6+12+18) -> ....
        if T == 1 + 3*(n-1)*n:
            print(n)
            break

        # e.g. 19 와 37 사이에 있는 경우
        elif T > 1 + 3*(n-1)*n and T < 1 + 3*n*(n+1):
            print(n+1)
            break
        # 다음 단계로 이동 : n 에 1 더하기
        else:
            n += 1


print(time.time()-start)
'''
# 테스트 케이스
T = int(input())

for tc in range(1, T+1):
    # x : 현재 위치 / y : 목표 위치
    x, y = map(int, input().split())

    # 작동 횟수
    cnt = 0

    # 출발할때 이동 가능한 광년 수(최대값)
    add = 1

    ##### 코드 다시 작성하기!!!!
    # (y-1) 위치를 거쳐가고, y에 도착해야 함(마지막에는 반드시 1 이동)
    # add 값이 2,3,4,5,6,... 순서로 증가하다가 다시 5,4,3,2,1로 감소할 경우에도 조건 만족 가능
    # x + add 값이 (y-1) 위치에 도달하지 못했을 때, while 문 진행
    while x + add < y-1:
        x += add
        cnt += 1

        # add 값이 2일 경우
        if add == 2:
            # x + add 가 (y-1) 위치에 도달하면 add 값 유지
            # 도달하지 못하면, add 값에 1 더하기
            if x + add < y-1:
                add += 1

        # add 값이 3일 경우
'''

T = int(input())

for _ in range(1, T+1):
    # x : 출발 지점 / y : 도착 지점
    x, y = map(int, input().split())

    # 총 이동해야 할 거리
    distance = y - x

    # 이동 횟수
    cnt = 0

    # 이동한 거리
    move = 0

    # 특정 cnt에서 이동 가능한 거리
    move_possible = 1

    while move < distance:
        cnt += 1
        move += move_possible
        if cnt % 2 == 0:
            move_possible += 1

    print(cnt)
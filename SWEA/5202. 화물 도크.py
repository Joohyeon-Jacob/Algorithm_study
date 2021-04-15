import sys
sys.stdin = open('sample_input_화물 도크.txt', 'r')

# 테스트 케이스
T = int(input())

for tc in range(1, T+1):
    # N : 신청서 -> 작업 수 표시
    N = int(input())

    # 작업 시작(s) & 종료(e) 시간 담을 리스트
    time_slot = []
    for _ in range(N):
        time_slot.append(list(map(int, input().split())))

    # lambda를 이용해서 정렬 -> lambda 원리 더 공부하기!!
    time_slot.sort(key=lambda x: (x[1], x[0]))

    # 24시간 동안 운용 가능한 화물차 수
    cnt = 0

    # 시작 : start / 종료 : end
    start = 0
    end = 0

    for slot in time_slot:
        if slot[0] >= end:
            start = slot[0]
            end = slot[1]
            cnt += 1

    print(f'#{tc} {cnt}')

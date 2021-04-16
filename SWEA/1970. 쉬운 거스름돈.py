import sys
sys.stdin = open('input_쉬운 거스름돈.txt', 'r')

# 테스트 케이스
T = int(input())

for tc in range(1, T+1):
    # 금액 단위별 필요한 개수 표시할 dict
    money_type = {
        50000: 0,
        10000: 0,
        5000: 0,
        1000: 0,
        500: 0,
        100: 0,
        50: 0,
        10: 0
    }

    # N : 금액
    N = int(input())

    print(f'#{tc}')
    # key(money), value(count) 순회
    for money, count in money_type.items():

        # 특정 money 필요한 개수(value 값) 업데이트
        count = N // money

        # 특정 money 가 사용 여부 반영해서, N 업데이트
        N -= money * count

        # value 값 출력
        print(count, end=' ')

    print()

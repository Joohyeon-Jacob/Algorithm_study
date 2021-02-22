import sys
sys.stdin = open('input_수도 요금 경쟁.txt','r')

# 테스트 케이스
T = int(input())

for tc in range(1, T+1):
    # A 사의 요금 : 1L 당 요금 = P
    # B 사의 요금 : R 리터 이하 -> 기본요금 Q 만 청구 / R 리터 초과 -> 1L 당 요금 = S 추가 납부
    # 이번달에 사용한 수도의 양 = W 리터
    P, Q, R, S, W = map(int, input().split())

    # A사 선택했을 때 내는 요금
    cost_A = P * W

    # B 사 선택했을 때 내는 요금
    # W <= R
    if W <= R:
        cost_B = Q
    # W > R
    else:
        cost_B = Q + S * (W - R)

    print('#{}'.format(tc), end=' ')

    if cost_A < cost_B:
        print(cost_A)
    else:
        print(cost_B)

# 가로 20 줄어들면서 재귀 방식으로 풀기

import sys
sys.stdin = open('sample_input_종이붙이기.txt','r')

# 테스트 케이스
T = int(input())

def placing(N):
    if N == 10:
        return 1
    elif N == 20:
        return 3
    else:
        return placing(N-10) + 2*placing(N-20)
'''
홀수, 짝수 나눠서 하다가 겹치는 경우가 발생한다는 것을 알았습니다.
그런데 해결을 못하다가.. 오우님 설명 듣고 해결했습니다^^
    # N = 10 * (홀수) 일때
    if (N//10) % 2 == 1:
        if N == 10:
            return 1
        else:
            return 4*placing(N-20) + 1
    
    # N = 10 * (짝수) 일때
    else:
        if N == 20:
            return 3
        else:
            return 4*placing(N-20) + 3
'''

for tc in range(1, T+1):
    # 20 * N 크기의 직사각형
    N = int(input())
    result = placing(N)

    print('#{} {}'.format(tc, result))
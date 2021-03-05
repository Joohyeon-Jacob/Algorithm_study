import sys
sys.stdin = open('input_암호생성기.txt','r')

# 테스트 케이스
T = 10

for tc in range(1, T+1):
    # 테스트 케이스 번호
    N = int(input())

    # 8개 숫자
    numbers = list(map(int, input().split()))

    # 배열의 마지막 숫자가 0이 되면 종료
    while numbers[-1] > 0:
        # 한 사이클 : 1 ~ 5 순회
        for i in range(1, 6):
            # 맨 앞 숫자 -> 타깃
            a = numbers.pop(0)

            # (타깃 - i)의 값이 0 보다 크면 그 값을 배열 마지막에 추가
            if a - i > 0:
                numbers.append(a-i)

            # 0 이하가 되면 0 추가하고 종료
            else:
                numbers.append(0)
                break

    print('#{}'.format(tc), end=' ')
    for code in numbers:
        print(code, end=' ')
    print()

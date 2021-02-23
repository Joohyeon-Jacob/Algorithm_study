import sys
sys.stdin = open('sample_input_괄호검사.txt','r')

# 테스트 케이스
T = int(input())

for tc in range(1, T+1):

    # 문자열 입력
    N = input()

    # stack
    s = []

    # top1 -> -1 이면 {} 가 없는 상태!!
    top1 = -1

    # top2 -> -1 이면 () 가 없는 상태!!
    top2 = -1

    # 문자열 순회 -> {}, () 짝 검사
    for char in N:
        # 중괄호 열릴 때 : s에 추가 & top1 업데이트
        if char == '{':
            s.append(char)
            top1 += 1

        # 괄호 열릴 때 : s에 추가 & top2 업데이트
        elif char == '(':
            s.append(char)
            top2 += 1

        # 중괄호 닫힐 때 : s의 마지막 원소가 { 인지 확인 & top1 업데이트
        elif char == '}':
            if len(s) != 0 and s[-1] == '{':
                # 마지막 원소 제거
                s.pop()
                top1 -= 1
            else:
                # 실패
                result = 0
                break

        # 괄호 닫힐 때 : s의 마지막 원소가 ( 인지 확인 & top2 업데이트
        elif char == ')':
            if len(s) != 0 and s[-1] == '(':
                # 마지막 원소 제거
                s.pop()
                top2 -= 1
            else:
                # 실패
                result = 0
                break

    # 문자열 순회가 break 없이 끝났을때 -> top1, top2 모두 -1 인지 확인
    else:
        if top1 == -1 and top2 == -1:
            result = 1
        else:
            result = 0

    print('#{} {}'.format(tc, result))
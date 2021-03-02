# import sys
# sys.stdin = open('sample_input_Forth.txt','r')

'''
함수 시도해보다가 정리 안 되서 그냥 조건문으로 코딩..

def forth(l): # l : 연산코드 담은 리스트

    for i in range(len(l)-1):

        # 연산자 만났을 때
        if l[i] == '+':
            # 맨 끝 숫자 2개 pop
            a = s.pop()
            b = s.pop()
            # 다시 stack에 추가
            s.append(int(a)+int(b))

        else:
            s.append(l[i])

    return s
'''

# 테스트 케이스
T = int(input())

for tc in range(1, T+1):
    # 숫자 담을 stack
    s = []

    # 256자 이내의 연산코드
    # calculation = input().split()
    calculation = list(map(str, input().split()))
    # print(calculation)

    for i in range(len(calculation)-1):
        if calculation[i] == '+':
            if len(s) >= 2:
                a = s.pop()
                b = s.pop()
                s.append(int(b)+int(a))
            else:
                s = []
                break

        elif calculation[i] == '-':
            if len(s) >= 2:
                a = s.pop()
                b = s.pop()
                s.append(int(b)-int(a))
            else:
                s = []
                break

        elif calculation[i] == '*':
            if len(s) >= 2:
                a = s.pop()
                b = s.pop()
                s.append(int(b)*int(a))
            else:
                s = []
                break

        elif calculation[i] == '/':
            if len(s) >= 2:
                a = s.pop()
                b = s.pop()
                s.append(int(b)//int(a))
            else:
                s = []
                break

        # 숫자(문자열) -> stack 에 push
        else:
            s.append(calculation[i])

    print('#{}'.format(tc), end=' ')

    # stack 에 숫자 하나만 들어있을 경우에만 출력 가능
    if len(s) == 1:
        print(s[0])
    else:
        print('error')
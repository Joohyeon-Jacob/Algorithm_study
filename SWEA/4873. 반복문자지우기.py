import sys
sys.stdin = open('sample_input_반복문자지우기.txt','r')

# 테스트 케이스
T = int(input())

for tc in range(1, T+1):
    # 문자열
    N = list(input())

    # 문자열 한 글자씩 담을 리스트
    letter_list = []

    # 재귀로는 어떻게 풀까?
    for char in N:
        if len(letter_list) == 0:
            letter_list.append(char)
        # 리스트의 마지막 원소와 같으면, 기존의 마지막 원소도 제거
        elif char == letter_list[-1]:
            letter_list.pop()
        else:
            letter_list.append(char)

    print('#{} {}'.format(tc, len(letter_list)))
import sys
sys.stdin = open('sample_input_정식이의 은행업무.txt', 'r')

# 2진수 숫자의 특정 숫자 바꾸기
def change_bin(num1): # num1 : bin_num
    for i in range(len(num1)):
        # '0'일 경우
        if num1[i] == '0':
            # '1'로 변환
            num1[i] = '1'
            bin_list.append(''.join(num1))
            # 되돌리기
            num1[i] = '0'
        else:
            num1[i] = '0'
            bin_list.append(''.join(num1))
            # 되돌리기
            num1[i] = '1'

# 3진수 숫자의 특정 숫자 바꾸기
def change_tri(num2): # num2 : tri_num
    for i in range(len(num2)):
        # '0'일 경우 -> '1' or '2'로 변경
        if num2[i] == '0':
            # '1'로 변경
            num2[i] = '1'
            tri_list.append(''.join(num2))
            # 되돌리기
            num2[i] = '0'

            # '2'로 변경
            num2[i] = '2'
            tri_list.append(''.join(num2))
            # 되돌리기
            num2[i] = '0'

        # '1'일 경우 -> '0' or '2'로 변경
        elif num2[i] == '1':
            # '0'로 변경
            num2[i] = '0'
            tri_list.append(''.join(num2))
            # 되돌리기
            num2[i] = '1'

            # '2'로 변경
            num2[i] = '2'
            tri_list.append(''.join(num2))
            # 되돌리기
            num2[i] = '1'

        # '2'일 경우 -> '0' or '1'로 변경
        else:
            # '0'로 변경
            num2[i] = '0'
            tri_list.append(''.join(num2))
            # 되돌리기
            num2[i] = '2'

            # '1'로 변경
            num2[i] = '1'
            tri_list.append(''.join(num2))
            # 되돌리기
            num2[i] = '2'

# 테스트 케이스
T = int(input())

for tc in range(1, T+1):
    # 2진수 / 3진수
    bin_num = list(input())
    tri_num = list(input())

    bin_list = []
    tri_list = []

    # 2진수 숫자 바꿔서 가능한 수 완성
    change_bin(bin_num)

    # 3진수 숫자 바꿔서 가능한 수 완성
    change_tri(tri_num)

    for i in range(len(bin_list)):
        # 2진수를 10진수로 변환
        bin_list[i] = int(bin_list[i], 2)

    for j in range(len(tri_list)):
        # 3진수를 10진수로 변환
        tri_list[j] = int(tri_list[j], 3)

    for value in bin_list:
        # bin_list의 원소인 value가 tri_list에도 존재한다면 그 수가 바로 찾는 답(ans)
        if value in tri_list:
            ans = value
            print(f'#{tc} {ans}')

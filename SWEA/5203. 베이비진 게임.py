import sys
sys.stdin = open('sample_input_베이비진 게임.txt', 'r')

# 연속인 숫자가 3개 이상이면 run, 같은 숫자가 3개 이상이면 triplet

def baby_gin(num_list): # num_list : 주어진 숫자 리스트
    # 숫자 리스트 길이가 3 이상이어야 판단 가능
    if len(num_list) < 3:
        return False

    # 0~9 까지의 숫자 각각의 빈도 체크
    cnt = [0]*10

    for num in num_list:
        cnt[num] += 1

    # run 체크(연속으로 3개 숫자 등장 여부 체크)
    aligned_num = 0

    for value in cnt:
        # triplet 인 경우
        if value == 3:
            return True

        # 특정 숫자 존재할 경우
        elif value:
            # 연속으로 등장하는 숫자 횟수 업데이트
            aligned_num += 1

        else:
            # 연속으로 등장하는 숫자 횟수 초기화
            aligned_num = 0

        # run 인 경우
        if aligned_num == 3:
            return True

# 테스트 케이스
T = int(input())

for tc in range(1, T+1):
    card_list = list(map(int, input().split()))

    # 1, 2번 플레이어 가져가는 카드 리스트
    card_list1 = []
    card_list2 = []

    # 게임 결과 -> 초기값 : 무승부
    result = 0

    for i in range(len(card_list)):
        # 홀수 번째 숫자(짝수 index) -> 1번 플레이어에 추가
        if i % 2 == 0:
            card_list1.append(card_list[i])

        else:
            card_list2.append(card_list[i])

        # 매번 숫자를 추가할때마다 베이비진 검사

        # 1번 승리
        if baby_gin(card_list1):
            result = 1
            break

        # 2번 승리
        elif baby_gin(card_list2):
            result = 2
            break
    
    # 테스트 케이스 1개 계속 통과 못함 -> 1, 2 번 그 누구라도 승리하면 break로 종료하는 조건 넣어서 해결!!
    # 1, 2번 어느 누구도 승리하지 못하고 순회 끝나면, result = 0 상태 유지

    print('#{} {}'.format(tc, result))
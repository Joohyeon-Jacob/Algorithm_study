import sys
sys.stdin = open('sample_input_이진탐색.txt', 'r')

# 계속 일부 test case 만 통과... 수정 필요..
def binary_search(data, low, high, key):
    global cnt
    global status

    if low > high:
        return -1
    else:
        mid = (low + high) // 2
        if key == data[mid]:
            # 문제 조건 만족
            cnt += 1
            # status = 0
            # -> status 초기화 하면 해결될줄 알았는데 여전히 오류..
            return mid
        elif key < data[mid]:
            # 이전에 오른쪽에 있었는지 확인 & 왼쪽으로 status 업데이트
            if status == 1:
                cnt += 1
            status = -1
            binary_search(data, low, mid-1, key)
        else:
            # 이전에 왼쪽에 있었는지 확인 & 오른쪽으로 status 업데이트
            if status == -1:
                cnt += 1
            status = 1
            binary_search(data, mid+1, high, key)


T = int(input())

for tc in range(1, T+1):
    # 리스트 A, B에 들어있는 정수 개수
    N, M = map(int, input().split())

    list_A = list(map(int, input().split()))
    list_B = list(map(int, input().split()))

    # B에 속한 어떤 수가 A에 들어있으면서,
    # 동시에 탐색 과정에서 양쪽구간을 번갈아 선택하게 되는 숫자의 개수 확인
    cnt = 0

    # mid 기준 key 값이 왼쪽이면 -1, 오른쪽이면 1
    status = 0

    # 이진 탐색

    for num in list_B:
        if num in list_A:
            binary_search(list_A, 0, len(list_A)-1, num)
        # status 초기화
        # status = 0

    print(f'#{tc} {cnt}')
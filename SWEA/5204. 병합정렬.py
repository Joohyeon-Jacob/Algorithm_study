import sys
sys.stdin = open('sample_input_병합정렬.txt', 'r')

# 분할 과정
def merge_sort(data): # data -> 분할 대상 리스트

    # 길이가 1 이하면 바로 return
    if len(data) <= 1:
        return data

    # 분할 기준점
    middle_num = len(data) // 2
    left = data[:middle_num]
    right = data[middle_num:]

    # 재귀 : 분할된 리스트끼리 다시 merge_sort
    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):

    global cnt

    if left[-1] > right[-1]:
        cnt += 1

    # 병합 결과
    result = []

    # 왼쪽 시작 지점
    i = 0
    # 오른쪽 시작 지점
    j = 0

    while len(left) > i or len(right) > j:
        if len(left) > i and len(right) > j:
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        elif len(left) > i:
            result.extend(left[i:])
            # 왼쪽 시작 지점 업데이트
            i = len(left)

        elif len(right) > j:
            result.extend(right[j:])
            # 오른쪽 시작 지점 업데이트
            j = len(right)

    return result



# 테스트 케이스
T = int(input())

for tc in range(1, T+1):
    # 정수의 개수
    N = int(input())

    # 정수 리스트
    data = list(map(int, input().split()))

    # left 마지막 원소 > right 마지막 원소 인 경우 카운트
    cnt = 0

    # merge_sort 된 data의 중간 index 값 설정
    center = len(data) // 2

    print(f'#{tc} {merge_sort(data)[center]} {cnt}')
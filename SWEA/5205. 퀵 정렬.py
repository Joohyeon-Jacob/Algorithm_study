import sys
sys.stdin = open('sample_input_퀵 정렬.txt', 'r')

def quicksort(data, left, right): # data : 정렬할 리스트
    if left < right:
        # 시작 지점
        start = partition(data, left, right)
        quicksort(data, left, start-1)
        quicksort(data, start+1, right)

def partition(data, left, right):
    # pivot 설정
    pivot = data[left]
    i = left
    j = right

    while i <= j:
        while data[i] <= pivot:
            i += 1
            break
        while data[j] >= pivot:
            j -= 1
            break
        if i < j:
            data[i], data[j] = data[j], data[i]

    data[left], data[j] = data[j], data[left]
    return j

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    data = list(map(int, input().split()))

    # 퀵 정렬
    quicksort(data, 0, len(data)-1)

    print('#{} {}'.format(tc, data[N//2]))
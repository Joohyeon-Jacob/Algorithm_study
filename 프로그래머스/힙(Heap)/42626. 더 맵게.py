

'''
<시간 초과 풀이>
def solution(scoville, K):
    # 섞은 횟수
    mix_count = 0
    while len(scoville) > 1:
        scoville.sort()
        first = scoville.pop(0)
        second = scoville.pop(0)
        new_num = first + second * 2
        scoville.insert(0, new_num)
        mix_count += 1
        if min(scoville) > K:
            return mix_count

    if len(scoville) == 1:
        return -1
'''
import heapq
# heapq : 가지고 있는 요소를 push, pop 할 때마다 자동으로 정렬

def solution(scoville, K):
    heap = []
    for num in scoville:
        heapq.heappush(heap, num)

    mix_count = 0
    while heap[0] < K:
        try:
            heapq.heappush(heap, heapq.heappop(heap) + heapq.heappop(heap) * 2)
        # heap 길이가 1일 경우, try 구문 작업 수행 불가하므로 IndexError 발생
        except IndexError:
            return -1
        mix_count += 1

    return mix_count

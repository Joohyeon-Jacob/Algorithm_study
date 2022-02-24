
def solution(distance, rocks, n):
    answer = 0
    left, right = 0, distance

    rocks.sort()

    while left <= right:
        mid = (left+right) // 2
        # 제거할 돌 개수
        remove_stone = 0
        # 현재 체크하는 돌
        check_stone = 0

        for rock in rocks:
            if rock - check_stone < mid:
                remove_stone += 1
            else:
                # 체크하는 기준점(돌) 이동
                check_stone = rock
            if remove_stone > n:
                break
        if remove_stone > n:
            right = mid - 1
        else:
            answer = mid
            left = mid + 1

    return answer

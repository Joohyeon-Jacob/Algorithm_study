
# https://sohee-dev.tistory.com/123

def solution(n, times):
    answer = 0

    # 최대 : 모두 가장 오래 걸리는 심사관에게 심사 받는 경우
    left, right = 1, max(times) * n

    while left <= right:
        mid = (left+right) // 2
        people = 0

        for time in times:
            people += mid // time
            if people >= n:
                break

        if people >= n:
            answer = mid
            right = mid - 1

        else:
            left = mid + 1

    return answer

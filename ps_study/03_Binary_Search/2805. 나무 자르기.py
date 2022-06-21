
if __name__ == "__main__":
    # 나무의 수 : N, 가져가야 할 나무의 길이 : M
    N, M = map(int, input().split())

    # 나무의 높이
    height_list = list(map(int, input().split()))

    left, right = 0, max(height_list)

    while left <= right:
        addition = 0
        # 절단기 높이 설정(이분탐색)
        mid = (left+right) // 2
        for height in height_list:
            if height > mid:
                addition += height - mid

        if addition >= M:
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    print(result)

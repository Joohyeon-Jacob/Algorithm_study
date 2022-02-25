
# https://haerang94.tistory.com/144

if __name__ == "__main__":
    # 강의 개수 : N, 블루레이 개수 : M
    N, M = map(int, input().split())

    lecture_times = list(map(int, input().split()))

    # 블루레이 크기 최소값 : 강의 길이 최대값
    left = max(lecture_times)

    # 블루레이 크기 최대값 : 강의 길이 총 합
    right = sum(lecture_times)

    # 블루레이 한 개 크기
    size = right
    while left <= right:
        mid = (left+right) // 2
        # 강의 전체 담기 위해 필요한 블루레이 개수 계산
        cnt = 0
        addition = 0
        for i in range(N):
            if addition + lecture_times[i] > mid:
                cnt += 1
                addition = 0
            addition += lecture_times[i]
        if addition:
            cnt += 1

        # 필요한 플루레이 개수가 M 보다 많은 경우, mid 증가 필요
        if cnt > M:
            left = mid + 1
        else:
            size = min(size, mid)
            right = mid - 1

    print(size)


def solution(n, lost, reserve):
    # 체육복 가져왔지만, 도난 당한 학생 목록 제거
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)

    # reserve 목록 탐색
    for num in set_reserve:
        if num - 1 in set_lost:
            set_lost.remove(num - 1)
        elif num + 1 in set_lost:
            set_lost.remove(num + 1)
        else:
            pass

    return n - len(set_lost)

result = solution(5, [1,4], [3])
print(result)
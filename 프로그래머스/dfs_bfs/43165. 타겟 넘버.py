
def solution(numbers, target):
    length = len(numbers)
    # 조합 가능한 경우의 수
    answer = 0

    def dfs(idx, result):
        if idx == length:
            if result == target:
                nonlocal answer
                answer += 1
            return
        else:
            dfs(idx+1, result+numbers[idx])
            dfs(idx+1, result-numbers[idx])
    dfs(0,0)

    return answer

print(solution([1, 1, 1, 1, 1], 3))
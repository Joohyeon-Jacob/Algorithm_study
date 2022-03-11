
def solution(people, limit):
    # 보트 운행 횟수
    count = 0

    people.sort()

    # 가장 가벼운 사람과 무거운 사람 태우기
    left = 0
    right = len(people) - 1
    while left < right:
        if people[left] + people[right] <= limit:
            left += 1
            right -= 1
        else:
            right -= 1
        count += 1
    if left == right:
        count += 1

    return count

result = solution([70, 80, 50], 100)
print(result)

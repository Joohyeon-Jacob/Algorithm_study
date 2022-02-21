
def solution(numbers):
    # 각 원소를 str 형태로 변환
    numbers = list(map(str, numbers))

    # numbers 의 원소가 1000 이하라는 점 이용
    numbers.sort(key=lambda x: x * 3, reverse=True)
    answer = str(int(''.join(numbers)))

    return answer

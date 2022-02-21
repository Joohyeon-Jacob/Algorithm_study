
# letter_to_num = [i for i in range(10)]

if __name__ == "__main__":
    # 단어의 개수
    N = int(input())
    letter_list = []

    for _ in range(N):
        letter_list.append(input())

    # 각 알파벳별로 합 최대로 만드는 과정에 기여하는 값 계산
    pow_str = [0] * 26
    for i in range(N):
        power = 1
        for char in reversed(letter_list[i]):
            pow_str[ord(char) - ord('A')] += power
            power = power * 10

    pow_str.sort(reverse=True)

    # 문자열 숫자로 전환한 합 최대값
    total_sum = 0

    # 기여도 높은 순서로 배열된 pow_str --> 앞에서부터 9 부여
    current_num = 9
    for p in pow_str:
        total_sum += p * current_num
        current_num -= 1

    print(total_sum)

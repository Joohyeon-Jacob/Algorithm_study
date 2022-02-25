
def solution(answers):
    answer = []
    correct_cnt_1, correct_cnt_2, correct_cnt_3 = 0, 0, 0
    length = len(answers)

    first_list = [1, 2, 3, 4, 5]
    second_list = [2, 1, 2, 3, 2, 4, 2, 5]
    third_list = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    # 1번 찍는 방식 주기 : 5
    # 2번 찍는 방식 주기 : 8
    # 3번 찍는 방식 주기 : 10

    for i in range(length):
        if answers[i] == first_list[i % 5]:
            correct_cnt_1 += 1
        if answers[i] == second_list[i % 8]:
            correct_cnt_2 += 1
        if answers[i] == third_list[i % 10]:
            correct_cnt_3 += 1

    result_list = [correct_cnt_1, correct_cnt_2, correct_cnt_3]
    max_result = max(result_list)

    for i in range(3):
        if result_list[i] == max_result:
            answer.append(i+1)

    return answer

print(solution([1, 2, 3, 4, 5]))
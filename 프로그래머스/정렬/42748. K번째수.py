
def solution(array, commands):
    answer = []

    # commands 순회
    for command in commands:
        start = command[0] - 1
        end = command[1]
        target_num = command[2] - 1
        # array 일부분
        temp_array = array[start:end]
        temp_array.sort()
        answer.append(temp_array[target_num])

    return answer

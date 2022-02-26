
from itertools import permutations

def solution(numbers):
    answer = []
    length = len(numbers)
    nums = [n for n in numbers]
    # 숫자 조합 추가
    perms = []
    for i in range(1, length+1):
        perms.extend(permutations(nums, i))
    new_nums = [int(''.join(p)) for p in perms]

    for new_num in new_nums:
        if new_num < 2:
            continue
        # 소수인지 체크
        check = True
        for i in range(2, int(new_num**0.5)+1):
            if new_num % i == 0:
                check = False
                break
        if check:
            answer.append(new_num)

    return len(set(answer))


# from itertools import combinations --> 시간 초과

def solution(number, k):
    # stack
    answer = []

    for num in number:
        if not answer:
            answer.append(num)
            continue
        if k > 0:
            while answer[-1] < num:
                answer.pop()
                k -= 1
                if not answer or k <= 0:
                    break
        answer.append(num)

    if k > 0:
        answer = answer[:-k]

    return ''.join(answer)


def count_triple_6(n, answer):
    cnt = 0
    while True:
        if '666' in str(answer):
            cnt += 1
        if cnt == n:
            return answer
        answer += 1

if __name__ == "__main__":
    N = int(input())

    answer = 666
    result = count_triple_6(N, answer)

    print(result)
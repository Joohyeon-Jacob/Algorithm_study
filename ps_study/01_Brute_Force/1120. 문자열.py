
def distance(A, B):
    if len(A) != len(B):
        return -1
    ret = 0
    for j in range(len(A)):
        if A[j] != B[j]:
            ret += 1
    return ret


if __name__ == "__main__":
    # 두 문자열
    A, B = map(str, input().split())

    length_A = len(A)
    length_B = len(B)

    answer = length_A

    for i in range(length_B - length_A + 1):
        diff = distance(A, B[i:(i+length_A)])
        if diff < answer:
            answer = diff

    print(answer)

# def A_B_count(K):
#     if K == 1:
#         return [0, 1]
#     else:
#         a = A_B_count(K-1)[1]
#         b = sum(A_B_count(K-1))
#         return [a, b]


if __name__ == "__main__":
    K = int(input())
    a = [1, 0]
    b = [0, 1]

    for i in range(2, K+1):
        a_cnt = a[i-1] + a[i-2]
        a.append(a_cnt)
        b_cnt = b[i-1] + b[i-2]
        b.append(b_cnt)

    print(a[K], b[K])

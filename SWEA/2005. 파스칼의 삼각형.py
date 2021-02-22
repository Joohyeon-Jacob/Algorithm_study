# 테스트 케이스
T = int(input())

for tc in range(1, T+1):
    # 파스칼 삼각형의 크기
    N = int(input())

    # 파스칼 삼각형 초기값
    pascal = [[0]*x for x in range(1, N+1)]

    # 첫 줄은 항상 1
    pascal[0][0] = 1

    for i in range(1, N):
        # i 번째 행의 숫자의 개수 = i
        for j in range(i+1):
            # 행의 시작과 끝은 1
            if j == 0 or j == i:
                pascal[i][j] = 1
            # 왼쪽 위 숫자 + 오른쪽 위 숫자
            elif j >= 1 and j <= i-1:
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]

    print('#{}'.format(tc))

    for i in range(len(pascal)):
        for j in range(len(pascal[i])):
            print(pascal[i][j], end=' ')
        print()
    print()
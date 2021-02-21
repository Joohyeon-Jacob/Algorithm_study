# 수 입력
X = int(input())

# 현재 단계 수
n = 1

while True:
    # 단계 n 의 마지막 순서의 숫자인가?
    if X == n*(n+1) // 2:
        # 홀수 단계인가?
        if n % 2 == 1:
            print('{}/{}'.format(1,n))
        # 짝수 단계인가?
        else:
            print('{}/{}'.format(n,1))
        break

    # 단계 n의 마지막 수보다 크고, 단계 (n+1) 의 마지막 수보다 작다
    elif X > n*(n+1) // 2 and X < (n+1)*(n+2) // 2: # X : (n+1) 단계의 수
        # 단계 (n+1) 의 몇번째 수인지 확인
        a = X - n * (n + 1) // 2

        # (n+1) 이 홀수 단계인가?
        if (n+1) % 2 == 1:
            print('{}/{}'.format(n+2-a,a))
        # (n+1) 이 짝수 단계인가?
        else:
            print('{}/{}'.format(a,n+2-a))
        break

    # 다음 단계로 이동
    else:
        n += 1
        a = 0
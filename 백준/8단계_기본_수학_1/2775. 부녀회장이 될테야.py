
'''
재귀 함수로 시도했지만, 시간 초과 발생 -> 누적합 방식으로 풀이
# 테스트 케이스
T = int(input())

# 재귀 함수로 접근
def resident(k, n): # k층 n호 거주자 수
    if k == 0:
        return n
    elif n == 1:
        return 1
    else:
        cnt = 0
        for i in range(1, n+1):
            cnt += resident(k-1, i) # (k-1)층 1~n호 거주자 수 총합
        return cnt

for tc in range(1, T+1):
    # k층, n호
    k = int(input())
    n = int(input())

    print(resident(k, n))
'''

T = int(input())

for tc in range(1, T+1):
    # k, n : k층 n호
    k = int(input())
    n = int(input())

    # 0층 각 호수 거주자 리스트
    f0 = []

    # 0층 1~n 호 거주자 수 체크
    for i in range(1, n+1):
        f0.append(i)

    # k층 거주자 수 -> 0층에서 k만큼 층 수 올리기
    for _ in range(k):
        # k층 n호 거주자 수 -> (k-1)층 기준, n호의 현재 거주자 수에 바로 앞 호수까지의 거주자 수 모두 더하기
        for i in range(1, n):
            f0[i] += f0[i-1]
        # print(f0)

    # k층 n호의 거주자 수
    print(f0[-1])


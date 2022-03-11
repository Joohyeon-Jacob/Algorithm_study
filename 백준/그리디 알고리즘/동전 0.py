
import sys

if __name__ == "__main__":
    # N : 동전 종류 수 / K : 동전으로 만들 가치의 합
    N, K = map(int, sys.stdin.readline().split())
    coin_list = []

    for _ in range(N):
        coin_list.append(int(sys.stdin.readline()))

    # 필요한 동전의 개수
    count = 0
    # coin_list.sort(reverse=True)

    for coin in reversed(coin_list):
        count += K // coin
        K = K % coin
    print(count)

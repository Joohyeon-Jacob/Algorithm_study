
if __name__ == "__main__":
    N = int(input())
    money_get_time = list(map(int, input().split()))
    money_get_time.sort()

    # 모든 사람 기다리는 시간 합
    total_waiting_time = 0
    addition = 0

    for time in money_get_time:
        addition += time
        total_waiting_time += addition
    print(total_waiting_time)

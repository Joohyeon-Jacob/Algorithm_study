import sys
sys.stdin = open('sample_input_전기버스2.txt', 'r')

def dfs(idx, cnt, total): # total : 해당 정류소의 배터리 용량
    global result
    if idx + total >= len(battery_num):
        if result > cnt:
            result = cnt
        return
    elif result < cnt:
        return

    for i in range(idx+1, idx+total+1):
        dfs(i, cnt+1, battery_num[i])


T = int(input())

for tc in range(1, T+1):
    # 정류장 수 N / 정류장 수 (N-1) 별 배터리 용량
    data = list(map(int, input().split()))

    N = data[0]
    battery_num = data[1:]

    # 충전 횟수(1번 정류장에서 충전한 것 제외)
    result = len(battery_num)

    # dfs
    dfs(0, 0, battery_num[0])

    print('#{} {}'.format(tc, result))

# 수동 채널 변경
def change_with_select(m):
    result = 500000
    for i in range(1000000):
        if valid(i):
            dist = len(str(i)) + abs(i-m)
            if result > dist:
                result = dist
    return result

# 채널 누르는 것 가능한 지 체크
def valid(num):
    num_str = str(num)
    for i in range(len(num_str)):
        if num_str[i] in num_list:
            return False
    return True

if __name__ == "__main__":
    N = int(input())
    M = int(input())

    if M > 0:
        num_list = list(input().split())
    else:
        num_list = []

    # + / - 로만 이동
    answer = abs(N-100)

    # 직접 번호 눌러서 이동한 후, + / - 로 이동
    answer = min(answer, change_with_select(N))

    print(answer)

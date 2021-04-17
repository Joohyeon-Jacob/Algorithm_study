import sys
sys.stdin = open('sample_input_격자판의 숫자 이어 붙이기.txt', 'r')

# 동서남북 이동
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def dfs(r, c, num): # num : 일곱자리 숫자 시작 지점

    # 일곱자리 숫자 완성
    if len(num) == 7:
        result.add(num)
        return

    # 미완성일 경우
    else:
        for i in range(4):

            # 상하좌우 이동
            nr = r + dr[i]
            nc = c + dc[i]

            # index 초과하지 않을 경우
            if 0 <= nr < 4 and 0 <= nc < 4:
                # num 업데이트
                num += travel_list[nr][nc]
                dfs(nr, nc, num)

                # num -> 일곱 자리 숫자에서 초기 탐색 상태로 되돌리기(끝에 한 글자씩 제거)
                num = num[:-1]

# 테스트 케이스
T = int(input())

for tc in range(1, T+1):
    # 격자판 정보
    travel_list = [list(map(str, input().split())) for _ in range(4)]

    # 가능한 일곱 자리 숫자 담을 set
    result = set()

    # 4*4 리스트 탐색
    for i in range(4):
        for j in range(4):
            dfs(i, j, travel_list[i][j])

    print(f'#{tc} {len(result)}')
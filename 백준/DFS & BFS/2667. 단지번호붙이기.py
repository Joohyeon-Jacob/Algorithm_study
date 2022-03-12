
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def dfs(x, y):
    global house_count

    if map_list[x][y] == 1:
        house_count += 1
        # 조사 완료한 단지는 0으로 표시
        map_list[x][y] = 0
        for i in range(4):
            # 탐색 가능한 이동 경로인지 체크
            if possible_route(x+dx[i], y+dy[i]):
                dfs(x+dx[i], y+dy[i])
        return True
    return False

def possible_route(x, y):
    if (x >= 0 and x < N) and (y >= 0 and y < N):
        return True
    return False

if __name__ == "__main__":
    N = int(input())
    map_list = []
    for _ in range(N):
        map_list.append(list(map(int, input())))

    # 단지별 가구 수 모아놓은 리스트
    house_info = []

    # 각 단지별 가구 수
    house_count = 0

    for i in range(N):
        for j in range(N):
            if dfs(i, j):
                house_info.append(house_count)
                # 단지별로 순회 완료하면, 초기화
                house_count = 0

    print(len(house_info))
    house_info.sort()
    for info in house_info:
        print(info)
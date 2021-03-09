x, y, w, h = map(int, input().split())

# (x, y)에서 직사각형까지의 거리 리스트
distance = [x, y, w-x, h-y]

# 거리 최소값
min_distance = 1000

# 최소값 업데이트
for value in distance:
    if value < min_distance:
        min_distance = value

print(min_distance)
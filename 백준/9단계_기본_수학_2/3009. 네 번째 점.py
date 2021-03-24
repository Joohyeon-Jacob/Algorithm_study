# 세 점의 좌표
point_list = [list(map(int, input().split())) for _ in range(3)]

x_dict = {}
y_dict = {}

for i in range(len(point_list[0])):
    for j in range(len(point_list)):
        point = point_list[j][i]
        if i == 0:
            if point not in x_dict:
                x_dict[point] = 1
            else:
                x_dict[point] += 1

        else:
            if point not in y_dict:
                y_dict[point] = 1
            else:
                y_dict[point] += 1

for key in x_dict:
    if x_dict[key] == 1:
        print(key, end=' ')

for key in y_dict:
    if y_dict[key] == 1:
        print(key)
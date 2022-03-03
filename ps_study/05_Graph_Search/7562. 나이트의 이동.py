
import sys

dx_dy = [(-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1)]

def solve(start, end):
    answer = 0

    q = [start]
    check[start[0]][start[1]] = True

    while len(q) != 0:
        q_size = len(q)
        for i in range(q_size):
            current = q.pop(0)
            if current[0] == end[0] and current[1] == end[1]:
                return answer

            for temp in dx_dy:
                np = (current[0]+temp[0], current[1]+temp[1])
                if inside_board(np) and check[np[0]][np[1]] == 0:
                    q.append(np)
                    check[np[0]][np[1]] = 1

        answer += 1
    return answer


def inside_board(p):
    return 0 <= p[0] < length and 0 <= p[1] < length

if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for _ in range(T):
        length = int(sys.stdin.readline())
        start_x, start_y = map(int, sys.stdin.readline().split())
        start = (start_x, start_y)

        check = [[0] * length for _ in range(length)]

        end_x, end_y = map(int, sys.stdin.readline().split())
        end = (end_x, end_y)

        result = solve(start, end)
        print(result)
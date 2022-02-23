
if __name__ == "__main__":
    N = int(input())

    array = []

    for _ in range(N):
        point_info = list(map(int, input().split()))
        array.append(point_info)

    array.sort(key=lambda x: (x[0], x[1]))

    for numbers in array:
        for num in numbers:
            print(num, end=' ')
        print()

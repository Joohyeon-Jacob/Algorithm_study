
import sys

N = int(sys.stdin.readline())

array = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    array.append([x, y])

sorted_array = sorted(array, key=lambda x: (x[1], x[0]))

for element in sorted_array:
    print(*element)

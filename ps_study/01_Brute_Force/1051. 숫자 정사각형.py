
import sys

# N * M 행렬
N, M = map(int, sys.stdin.readline().split())
array = []

for _ in range(N):
    array.append(input())

answer = 1
for i in range(N):
    for j in range(M):
        for k in range(M if M>N else N):
            if i + k < N and j + k < M:
                if (array[i][j] == array[i+k][j] == array[i][j+k] == array[i+k][j+k]):
                    length = (k+1)**2
                    if length > answer:
                        answer = length
print(answer)

# 입력할 숫자의 개수
T = int(input())

# 공백없이 T 개 만큼 숫자 입력 : string 형태로
N = input()

# 총합
result = 0

# N을 정수열로 변환한 n
n = int(N)

while n:
    result += n % 10
    n = n // 10

print(result)
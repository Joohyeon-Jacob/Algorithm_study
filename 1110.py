# while 문 사용

# 더하기 사이클 N 구하기
# e.g. 26 : 26 -> 68 -> 84 -> 42 -> 26 --> N = 4 

# 사이클 확인할 숫자 입력
a = int(input())

# Target 값 도달하면 사이클 종료
Target = a

# 사이클 값 N 초기값
N = 0

while True:
    # a의 각 자리 수 더하기
    b = (a // 10) + (a % 10)

    # b의 일의 자리 수
    c = b % 10
    
    # 한 사이클 진행 완료
    a = 10 * (a % 10) + c
    N += 1
    
    # Target 과 a의 값이 같으면, 종료
    if a == Target:
        break
    else:
        continue

print(N)
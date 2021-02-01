# while 문 사용

# a + b 값 출력
# a=0 & b=0 일때, 종료

while True:
    a, b = map(int, input().split())
    c = a + b
    if a != 0 and b != 0:
        print(c)
    elif a == 0 and b == 0:
        break

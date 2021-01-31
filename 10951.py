# while 문 사용

# a + b 값 출력

while True:
    try:
        a, b = map(int, input().split())
        c = a + b
        print(c)
    except:
        break

# <try & except>

# try 아래의 코드블락(code block)이 실행된다.

# 예외가 발생되지 않으면, except없이 실행이 종료 된다.

# 예외가 발생하면, 남은 부분을 수행하지 않고, except가 실행된다.

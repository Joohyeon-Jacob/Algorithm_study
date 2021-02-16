# 테스트 케이스
T = int(input())

for tc in range(1, T+1):

    # b 문자열을 int(a) 횟수만큼 각 글자를 반복해서 출력하기
    a, b = input().split()

    for char in b:
        for _ in range(int(a)):
            print(char, end='')
    print()
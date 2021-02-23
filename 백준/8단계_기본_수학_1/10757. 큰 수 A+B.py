import sys
a, b = map(str, sys.stdin.readline().split())

list_a = list(a)
list_b = list(b)

a = len(list_a)
b = len(list_b)

c = int(list_a[-1]) + int(list_b[-1])

# a와 b를 더한 결과
result = 0

# 자리 수에 맞게 곱해줄 값 n -> 10^n
n = 0

# a 와 b 를 1씩 차감 -> 하나라도 먼저 0 이 되면 더 긴 리스트의 나머지 자리숫자 만큼만 더하기
while a > 0 and b > 0:
        result += (int(list_a.pop()) + int(list_b.pop()))*(10**n)
        # 남은 숫자 개수 1 감소
        a -= 1
        b -= 1
        # 자리 수 1 증가한것 반영
        n += 1
        # 현재 자리 수
        k = 10**n

# a는 0 이고 b > 0 인 경우
if a == 0 and b > 0:
    for j in range(b-1, -1, -1):
        result += int(list_b.pop())*k
        k = k*10

# a > 0 이고 b = 0 인 경우
if a > 0 and b == 0:
    for j in range(a-1, -1, -1):
        result += int(list_a.pop())*k
        k = k*10

print(result)



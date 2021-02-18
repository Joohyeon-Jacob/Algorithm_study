# 두 문자열(숫자 형태) 입력
a, b = input().split()

# 상수의 방식으로 a, b 읽은 결과 -> new_a, new_b
new_a = ''
new_b = ''

# 거꾸로 이어 붙이기
for char in a:
    new_a = char + new_a

for char2 in b:
    new_b = char2 + new_b

if int(new_a) > int(new_b):
    print(new_a)
else:
    print(new_b)


# A : 고정 비용
# B : 노트북 한 대 당 가변 비용

# C : 노트북 한 대 당 판매 수입

A, B, C = map(int, input().split())

# 노트북 대 수
x = 0

if B >= C:
    print(-1)

else:
    x = A//(C-B) + 1

    print(x)

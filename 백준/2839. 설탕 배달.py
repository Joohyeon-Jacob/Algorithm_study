# 설탕 배달 무게 : N
N = int(input())

# 5로 나눈 나머지
residue = N % 5

# answer : 봉지 수(불가능할 경우 -1)
answer = 0
if residue == 0:
    answer = N // 5
elif residue == 1:
    answer = (N-6) // 5 + 2
elif residue == 2:
    if N == 7:
        answer = -1
    else:
        answer = (N-12) // 5 + 4
elif residue == 3:
    answer = (N-3) // 5 + 1
else:
    if N == 4:
        answer = -1
    else:
        answer = (N-9) // 5 + 3

print(answer)
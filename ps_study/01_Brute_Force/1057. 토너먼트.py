
# 참가자의 수, 김지민의 번호, 임한수의 번호
N, A, B = map(int, input().split())

# 라운드 진행 수
count = 1

# 같은 그룹(대결 상대)로 묶이면 종료
while (A+1)//2 != (B+1)//2:
    A, B = (A+1)//2, (B+1)//2
    count += 1

print(count)
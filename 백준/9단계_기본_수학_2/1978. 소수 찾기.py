N = int(input())

# 소수 후보군 리스크
sosu = list(map(int, input().split()))

# 소수 개수 -> sosu 리스트 원소 모두 소수라고 가정
cnt = len(sosu)

# 소수인지 체크
for num in sosu:
    # num 이 1이면 소수 개수 1 차감
    if num == 1:
        cnt -= 1

    # 2부터 (num-1) 까지 수 중에 약수 있는지 확인
    else:
        for j in range(2, num):
            if num % j == 0:
                # 소수 개수 1 차감
                cnt -= 1
                break

print(cnt)
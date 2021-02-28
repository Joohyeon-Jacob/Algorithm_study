# 문자열 입력
T = list(input())

# 단어 개수 카운트
cnt = 0

# 단어 개수 = (단어 사이의)공백 개수 + 1

# 리스트 T 순회
for i in range(len(T)):
    # 공백을 만날 경우, 처음과 마지막 index 가 아니면, cnt 업데이트
    if T[i] == ' ' and i != 0 and i != len(T)-1:
        cnt += 1

# 리스트가 비어 있거나 or 공백만 들어 있을 경우
if len(T) == 0 or (len(T) == 1 and T[0] == ' '):
    print(cnt)
# 단어의 개수
else:
    print(cnt+1)
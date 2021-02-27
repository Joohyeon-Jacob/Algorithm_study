# 그룹 단어 개수
T = int(input())

# 그룹 단어 조건 만족하는 단어 개수
cnt = 0

for tc in range(1, T+1):
    # 그룹 단어
    word = list(input())

    # word 의 단어 각 글자를 중복 없이 담을 리스트 -> 답 : 리스트의 길이
    check = []

    for letter in word:
        # 처음에는 추가
        if len(check) == 0:
            check.append(letter)
        # check 리스트 마지막 원소와 letter 가 다를 경우
        elif letter != check[-1]:
            # check 리스트의 다른 원소와 letter 가 같으면 그룹 단어 조건 불만족
            if letter in check:
                check = []
                break
            # check 리스트에 letter 가 아예 없으면 새로운 원소로 추가
            else:
                check.append(letter)
        # check 의 마지막 원소와 letter 가 같을 경우 -> 그냥 추가
        else:
            check.append(letter)

    # check 에 모든 letter 가 들어오면, 그룹 단어 조건 만족
    if len(check) == len(word):
        cnt += 1

print(cnt)
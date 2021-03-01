# 크로아티아 문자열 종류
croatian_alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

# 알파벳 총 개수 결과
cnt = 0

# 문자열 입력 리스트
word = list(input())

while len(word) >= 3: # 뒤에서부터 순회 & 세 글자 남았을때까지 진행

    # 끝의 세 글자가 croatian_alphabet 의 원소일때
    if word[-3] + word[-2] + word[-1] in croatian_alphabet:
        word = word[:-3] # 슬라이싱

    # 끝의 두 글자가 croatian_alphabet 의 원소일때
    elif word[-2] + word[-1] in croatian_alphabet:
        word = word[:-2] # 슬라이싱

    # 둘 다 아닐때 -> 마지막 글자만 pop
    else:
        word.pop()

    # 단어 개수 업데이트
    cnt += 1

# word 리스트에 글자가 한 글자 남아 있을 경우
if len(word) == 1:
    cnt += 1

# word 리스트에 글자가 두 글자 남아 있을 경우
elif len(word) == 2:

    # 남은 글자들을 한 단어로 만들기
    check = ''.join(word)

    # 이 단어가 croatian_alphabet 의 원소일 경우
    if check in croatian_alphabet:
        cnt += 1

    # 아닐 경우 -> 2. 두 글자가 다르면
    else:
        cnt += 2

print(cnt)
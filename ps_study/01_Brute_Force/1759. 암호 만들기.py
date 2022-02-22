

def dfs(index, depth):
    global vowel, consonant, visited

    if depth == L:
        # 모음 개수(1) & 자음 개수(2) 조건 확인
        if vowel >= 1 and consonant >= 2:
            for i in range(C):
                # 방문 체크
                if visited[i]:
                    print(letter_list[i], end='')
            print()
        return

    for i in range(index, C):
        if not visited[i]:
            visited[i] = True
            if isVowel(letter_list[i]):
                vowel += 1
            else:
                consonant += 1

            dfs(i+1, depth+1)
            visited[i] = False

            if isVowel(letter_list[i]):
                vowel -= 1
            else:
                consonant -= 1


# 모음인지 체크
def isVowel(char):
    if char in ['a', 'e', 'i', 'o', 'u']:
        return True
    return False


if __name__ == "__main__":
    L, C = map(int, input().split())
    letter_list = input().split()
    # 문자열 정렬
    letter_list.sort()

    visited = [False] * C

    # 모음 & 자음 개수
    vowel, consonant = 0, 0
    dfs(0, 0)

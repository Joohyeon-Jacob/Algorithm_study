# 각 단어(알파벳 대문자)에 해당하는 숫자 모두 더하기 + (1x문자열 길이) 더하기

# print(ord('A'))
# print(ord('B'))
# print(ord('Y'))
# print(ord('Z'))

# 다이얼 입력 -> 암호의 특정 문자가 dial[i] 에 들어있으면, 다이얼 돌리는데 (i+3) 초 걸린다
dial = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'], ['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R', 'S'], ['T', 'U', 'V'], ['W', 'X', 'Y', 'Z']]

# 문자열 입력
T = list(input())

# 암호를 다이얼로 변환했을때 찾은 소요시간
result = 0

# 문자열 T 순회
for letter in T:
    # 특정 문자열을 다이얼로 돌릴때 걸리는 시간
    add = 0
    # dial 원소 순회
    for i in range(len(dial)):
        for j in range(len(dial[i])):
            # dial[i][j] 와 letter 가 같으면 result 업데이트
            if dial[i][j] == letter:
                add += i+3
                # result 에 add 추가하고 문자열 순회 종료
                result += add
                break
        # result 에 추가한 값이 있으면(add > 0), 다음 letter 로 이동
        if add > 0:
            break

print(result)
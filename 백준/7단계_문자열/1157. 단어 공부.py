# 문자열 입력
T = list(input())

# 문자열 전체를 대문자로 변환
for i in range(len(T)):
    # 소문자일 경우
    if ord(T[i]) >= 97 and ord(T[i]) <= 122:
        # 대문자로 변환
        T[i] = chr(ord(T[i])-32)

# T의 문자열 종류 담기(중복 제거)
check = {}
for letter in T:
    if letter not in check:
        check[letter] = 0

# check(dic) key 값의 value 업데이트
for letter2 in check:
    # T 리스트의 원소(letter3) 와 비교를 통해, 특정 key 값(letter2)이 등장하는 횟수 체크
    for letter3 in T:
        if letter3 == letter2:
            check[letter2] += 1

# 문자열 빈도수의 최대값 : result
# result 값을 value 로 가지고 있는 문자열 담는 리스트 : ans

result = 0
ans = []

# check 의 key 값 순회
for key in check:
    # 빈도 수(특정 key의 value 값) 최대값 갱신
    if check[key] > result:
        # ans 리스트 초기화하고, key 값을 담기
        ans = []
        ans.append(key)
        # 최대값(최대 빈도) 업데이트
        result = check[key]
    # 최대값과 같은 빈도수의 문자열 등장했을때
    elif check[key] == result:
        # ans 리스트에 그냥 추가
        ans.append(key)

# ans 리스트에 원소가 2개 이상(빈도수 최대인 원소가 2개 이상)
if len(ans) >= 2:
    print('?')

# 1개라면, 해당 원소 출력
else:
    print(ans[0])


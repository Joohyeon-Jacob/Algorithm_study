# 삼각형의 세 변 길이

while True:
    length_list = list(map(int, input().split()))
    if length_list[0] == 0:
        break
    # 가장 긴 변 제외한 나머지 길이들의 제곱의 합
    remain = 0
    # 가장 긴 변의 길이의 제곱
    longest = 0
    for i in range(len(length_list)):
        if length_list[i] > longest:
            longest = length_list[i] # 가장 긴 변 길이 업데이트
            longest_index = i # 가장 긴 변의 index 표시

    for j in range(len(length_list)):
        if j != longest_index:
            remain += length_list[j]**2

    if longest**2 == remain:
        print('right')

    else:
        print('wrong')

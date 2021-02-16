# 문자열
T = input()

# order 값 리스트
order = [x for x in range(ord('a'), ord('z')+1)]

# a ~ z의 ord 값으로 순회
for i in range(len(order)):

    # 앞에서 몇 번째 글자만에 나타나는지 확인 -> 초기값 = -1
    location_num = -1

    # T의 각 문자와 비교
    for char in T:
        # order[i] 와 ord(char) 이 같으면 location_num 1 더하고 break
        if ord(char) == order[i]:
            location_num += 1
            break

        # order[i] 와 ord(char) 이 달라도 앞에서부터의 위치 파악을 위해 location_num 에 1 더하기
        else:
            location_num += 1

    # break 문을 타지 않으면 location_num = -1로 설정
    else:
        location_num = -1

    print(location_num, end=' ')

# print(ord('a'))
# print(ord('z'))
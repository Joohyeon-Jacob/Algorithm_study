# 숫자 개수
N = int(input())

# 정렬 리스트
num_list = []

for _ in range(N):
    num_list.append(int(input()))

# i번째 index 해당 숫자 기준, 뒤에 있는 수들의 최소값과 비교 -> 최소값보다 크다면 swap
for i in range(len(num_list)-1):
    # 바로 뒤에 있는 수를 일단 최소값으로 설정
    min_value = num_list[i+1]
    # index 기록
    index = i+1
    for j in range(i+1, len(num_list)):
        if num_list[j] < min_value:
            min_value = num_list[j]
            # 최소값의 index 업데이트
            index = j
    # 최소값과 i번째 index 해당 숫자 비교
    if min_value < num_list[i]:
        # swap
        num_list[i], num_list[index] = num_list[index], num_list[i]

for num in num_list:
    print(num)
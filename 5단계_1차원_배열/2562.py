# 미완성!!!!

# 9개의 숫자 입력
# 첫째 줄에 최대값, 둘째 줄에 최대값이 몇 번째 수인지 출력

# 입력 받은 숫자 추가할 리스트
n = int(input())
nums = [int(input()) for _ in range(n)]

# for i in range(9):
#   a = int(input())
#   num_list.append(a)

# num_list의 최대값 초기 설정
max_number = num_list[0]

# max_number의 index
max_index = 0

for j in range(len(num_list)):
  if num_list[j] >= max_number:
    max_number = num_list[j]
    max_index = j

print(max_number)
print(j)
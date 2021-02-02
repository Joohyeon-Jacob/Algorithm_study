# 9개의 숫자 입력
# 첫째 줄에 최대값, 둘째 줄에 최대값이 몇 번째 수인지 출력

# 입력 받은 숫자 추가할 리스트
num_list = []

for i in range(9):
  n = int(input())
  num_list.append(n)

# num_list를 sorting한 List : getting_higher
getting_higher = sorted(num_list)
highest = getting_higher[-1] # num_list의 최대값

for j in range(len(num_list)):
  if num_list[j] == highest:
    print(highest)
    print(j+1)
  


# 42로 나눈 나머지 -> 서로 다른 나머지의 개수는?

# input 담을 List
num_list = []

for i in range(10):
  a = int(input())
  num_list.append(a)

# 42로 나눈 나머지 담을 List. 단, 중복 없이!!
r_list = []

for num in num_list:
  residue = num % 42
  if residue not in r_list: # 중복 피하기
    r_list.append(residue)

print(len(r_list))
    
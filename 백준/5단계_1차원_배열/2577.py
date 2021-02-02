a = int(input())
b = int(input())
c = int(input())

d = a*b*c

# 각 자리 숫자 담을 List
num_list = []

while d: # d > 0 일때
  num_list.append(d%10)
  d = d // 10

# count(i) 이용 -> i = 0 ~ 9 의 개수 확인
for i in range(10):
  cnt = num_list.count(i)
  print(cnt) 
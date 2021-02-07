# OX 퀴즈

N = int(input())

for i in range(N):
  # 결과 초기값
  result = 0
  a = 0
  ox_string = input()

  for char in ox_string:
    if char == 'O':
      a += 1
      result += a
    else:
      a = 0
  print(result) 



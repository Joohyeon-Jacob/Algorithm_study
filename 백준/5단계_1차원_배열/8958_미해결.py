# OX 퀴즈 --> 미해결!!

N = int(input())

for i in range(N):
  # 결과 초기값
  result = 0
  ox_string = str(input())

  for char in ox_string:
    a = 0
    while char == 'O':
      a += 1
    result += a*(a+1)//2
  print(result) 


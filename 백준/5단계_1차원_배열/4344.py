# 누구나 본인은 평균 이상이라고 생각한다

# Test case 개수
n = int(input())

for _ in range(n):
  numbers = list(map(int, input().split()))
  # 입력한 점수의 합
  score_sum = 0

  for j in range(1, len(numbers)):
    score_sum += numbers[j]
  
  # 평균 확인
  score_avg = score_sum / (len(numbers)-1)

  # 평균 넘는 수의 개수 초기값
  above_avg = 0

  # 평균 넘는 값 확인
  for k in range(1, len(numbers)):
    if numbers[k] > score_avg:
      above_avg += 1
  
  # answer = round((100*above_avg / (len(numbers)-1)), 3)
  answer = 100*above_avg / (len(numbers)-1)
  print('%.3f' % answer + '%')



# 예제 입력
# 5
# 5 50 50 70 80 100
# 7 100 95 90 80 70 60 50
# 3 70 90 80
# 3 70 90 81
# 9 100 99 98 97 96 95 94 93 91

# 예제 출력
# 40.000%
# 57.143%
# 33.333%
# 66.667%
# 55.556%
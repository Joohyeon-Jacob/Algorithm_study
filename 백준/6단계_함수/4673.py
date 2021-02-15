# 10000 이하의 셀프 넘버 개수 출력

# 33 -> 39(33 + 3 + 3) : 33은 39의 생성자

# 셀프 넘버 : 생성자가 없는 숫자

numbers = [x for x in range(1, 10001)]

# 셀프 넘버가 아닌 수의 리스트
not_self_numbers = []

# numbers 리스트 원소를 생성자로 활용
for num in numbers:
  new_number = num
  while num > 0:
    new_number += num % 10
    num = num // 10
  not_self_numbers.append(new_number)

# numbers 리스트 원소 중에 not_self_numbers 에 들어있지 않은 원소 출력

for num2 in numbers:
  if num2 not in not_self_numbers:
    print(num2)
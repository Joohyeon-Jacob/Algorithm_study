# 8자리 숫자로 YYYY/MM/DD 출력

# 8자리 숫자를 숫자 하나씩 분리해서 리스트 원소로 저장해놓는 방법은?

# 테스트 케이스 개수
n = int(input())

for i in range(n):

  # 입력하는 8자리 숫자
  a = int(input())
  
  
  # # DD 저장
  # b = a % 100 # 하지만, 이렇게 하면 02, 03 등의 0이 저장되지 않는다..
  # a = a // 100

  # # MM 저장
  # c = a % 100 # 하지만, 이렇게 하면 02, 03 등의 0이 저장되지 않는다..
  
  # # 월 - 일 조합 맞는지 체크!!

# 최소, 최대

# 정수 개수
a = int(input())

# 정수(a개만큼) 입력해서 List에 저장
numbers = [int(a) for a in input().split()]

# 오름차순 정렬
numbers.sort()

# 최소값 & 최대값
print(numbers[0], end=' ')
print(numbers[-1])
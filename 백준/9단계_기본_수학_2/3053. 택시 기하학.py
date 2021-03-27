import math

# 반지름 길이
r = int(input())

# 유클리드 기하학 원 넓이
s1 = math.pi*(r**2)

# 비유클리드 기하학 원 넓이
s2 = ((2*r)**2)*0.5

print(s1)
print(s2)
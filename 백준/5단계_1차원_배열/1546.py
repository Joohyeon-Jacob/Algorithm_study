# 새로운 평균

# 정수 개수 N
N = int(input())

# 정수 담을 List
num_list = [int(N) for N in input().split()]

# 최대값 d
d = sorted(num_list)[-1]

# 새로운 평균
new_avg = (sum(num_list)/d)*100/N

print(new_avg)
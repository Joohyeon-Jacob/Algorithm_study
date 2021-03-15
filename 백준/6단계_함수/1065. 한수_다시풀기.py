# # 한수 : 각 자리 숫자의 차이가 등차수열을 이루는 수
#
# # 1 이상 N 이하의 숫자 중에 한수의 개수를 찾아야 한다.
# N = int(input())
#
# # 한수 개수
# cnt = 0
#
# # 1 ~ N 탐색
# for num in range(1, N+1):
#     # N 이 한자리 수 or 두 자리 수면, 모두 한수
#     if num % 100 == 0:
#         cnt += 1
#
#     else:
#         num_list = []
#         while num:
#             num_list.append(num % 10)
#             num = num // 10
#
#         diff = num_list[1] - num_list[0]
#         diff_cnt = 0
#         for i in range(len(num_list)-1):
#             if num_list[i+1] - num_list[i] == diff:
#                 diff_cnt += 1
#             else:
#                 break
#
#         if diff_cnt == len(num_list)-1:
#             cnt += 1
#
# print(cnt)

num = int(input())
hansu = 0

for n in range(1, num + 1):
    if n <= 99:  # 1부터 99까지는 모두 한수
        hansu += 1

    else:
        nums = list(map(int, str(n)))  # 숫자를 자릿수대로 분리
        if nums[0] - nums[1] == nums[1] - nums[2]:  # 등차수열 확인
            hansu += 1

print(hansu)
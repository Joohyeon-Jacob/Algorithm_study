from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = 0
        for i in range(1, len(prices)):
            if prices[i] < prices[buy]:
                # 매수 시점 업데이트
                buy = i
            else:
                diff = prices[i] - prices[buy]
                if diff > profit:
                    # 최대 이익 업데이트
                    profit = diff
        return profit

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#
#         length = len(prices)
#         check_dict = {}
#
#         for num in prices:
#             # 차이 최대값 초기 설정 : 0
#             check_dict[num] = 0
#
#         for i in range(length):
#             for j in range(i+1, length):
#                 # 중복된 숫자 loop 생략
#                 if prices[j] == prices[i]:
#                     pass
#                 elif prices[j]-prices[i] > check_dict[prices[i]]:
#                     new_value = prices[j]-prices[i]
#                     # value 업데이트
#                     check_dict[prices[i]] = new_value
#
#         # value 기준으로 sort
#         sorted_tuples = sorted(check_dict.items(), key=lambda item: item[1], reverse=True)
#         answer = sorted_tuples[0][1]
#
#         return answer

result = Solution()
print(result.maxProfit(prices = [2,1,2,0,1]))
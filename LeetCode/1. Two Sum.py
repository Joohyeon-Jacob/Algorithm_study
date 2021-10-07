from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)

        for i in range(length):
            # 다음 index 부터 순회
            for j in range(i+1, length):
                if nums[i] + nums[j] == target:
                    return [i, j]

result = Solution()
print(result.twoSum(nums = [2,7,11,15], target = 9))
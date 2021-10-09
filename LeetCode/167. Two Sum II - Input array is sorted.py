from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums : 이미 정렬된 리스트
        i = 0
        l = len(nums)-1
        while i < l:
            check = nums[i] + nums[l]
            if check < target:
                # 더 큰 수로 이동
                i += 1
            elif check > target:
                # 더 작은 수로 이동
                l -= 1
            elif check == target:
                return [i+1, l+1]


result = Solution()
print(result.twoSum(nums = [-3,3,4,90], target = 0))
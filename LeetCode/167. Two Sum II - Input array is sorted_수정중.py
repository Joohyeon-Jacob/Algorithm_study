from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 순회 범위 : length
        length = 0

        # 이미 sorted 되어 있음 -> target 이상인 원소 위치 찾고, 그 전까지 순회하기
        for idx, num in enumerate(nums):
            if num >= target:
                length = idx
                break

        # 모든 원소가 target 이하일 경우 -> nums 전체 순회
        if not length:
            length = len(nums)

        for i in range(length):
            # 다음 index 부터 순회
            for j in range(i+1, length):
                if nums[i] + nums[j] == target:
                    # (idx+1) 값 return
                    return [i+1, j+1]

result = Solution()
print(result.twoSum(nums = [2,3,4], target = 6))
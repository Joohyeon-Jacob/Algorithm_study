from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # 정렬
        nums.sort()
        result = 0
        for i in range(0, len(nums), 2):
            # 배열의 숫자들을 두 개씩 짝 지어서 "각각의 최소값들의 합"의 최대값을 구하기
            # 첫 번째 원소(nums[0])와의 조합에서 최소값은 무조건 첫 번째 원소.
            # 따라서 바로 다음 원소와 조합을 이루어야 한다.
            # 해당 두 원소를 제거한 리스트에서 같은 과정 반복
            result += nums[i]

        return result

value = Solution()
print(value.arrayPairSum([1,4,3,2]))

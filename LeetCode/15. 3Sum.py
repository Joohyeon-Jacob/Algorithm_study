from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # triplet 조합 리스트를 담을 리스트
        triplet_list = []
        
        # 반복 피하기 위해 정렬
        nums.sort()

        length = len(nums)
        for i in range(length-1):
            
            # nums 원소 중 체크 완료한 원소 담는 리스트
            checked_num = set()
            
            # triplet 조합 찾기 위한 임시 생성 리스트
            temp_list = []

            # 첫 번째 원소 추가
            temp_list.append(nums[i])

            # 0 - (선택한 원소)
            residue = 0 - nums[i]

            for j in range(i+1, length):

                if (residue - nums[j]) in checked_num:

                    # 합이 0이 되도록 하는 조합 완성
                    temp_list.append(nums[j])
                    temp_list.append(residue - nums[j])

                    # 완성한 temp_list 를 triplet_list에 추가
                    if list(temp_list) not in triplet_list:
                        triplet_list.append(list(temp_list))

                    # 추가한 두 개 숫자 제거
                    temp_list.pop(2)
                    temp_list.pop(1)
                checked_num.add(nums[j])

        return triplet_list


lst = [-1,0,1,2,-1,-4]
result = Solution()
print(result.threeSum(lst))
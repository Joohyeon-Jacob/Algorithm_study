from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)

        # product 결과 리스트 초기 설정
        products_list = [0 for _ in range(length)]

        product = 1

        # 0의 idx를 표시(담을) 리스트
        check_zero_idx = []

        for i in range(length):
            if nums[i] == 0:
                # 이미 0인 원소의 idx 존재할 경우 -> 0인 원소가 2개이므로 순회 중지
                if len(check_zero_idx) >= 1:
                    return products_list

                # 0이 처음 등장한 경우
                else:
                    check_zero_idx.append(i)

            # 0을 제외하고 모두 곱한 값 업데이트
            else:
                product *= nums[i]

        # nums 에 0이 하나 존재할 경우
        if check_zero_idx:
            products_list[check_zero_idx[0]] = product

        # nums 에 0이 존재하지 않을 경우
        else:
            for idx, num in enumerate(nums):
                # product에서 idx에 해당하는 num 을 0에서 해당 num 값으로 업데이트
                products_list[idx] = product // num

        return products_list

answer = Solution()
answer2 = Solution()
print(answer.productExceptSelf([1,2,3,4]))
print(answer2.productExceptSelf([-1,1,0,-3,3]))
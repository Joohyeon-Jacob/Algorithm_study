from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # 순회 범위 : loop
        loop = (len(s)-1) // 2

        # index --> 0 ~ loop 까지 순회
        for i in range(loop+1):
            s[i], s[len(s)-1-i] = s[len(s)-1-i], s[i]

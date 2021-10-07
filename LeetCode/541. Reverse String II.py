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

        return s

    def reverseStr(self, s: str, k: int) -> str:
        # s : 문자열, k : 초반에 바꿀 문자 길이
        # 순회 단위 : 2k

        # 현재 순회 index 위치 : i
        # 문자열 결과 : result
        s_list = list(s)
        i = 0
        length = len(s_list)
        # while length > i+2k:
        #     # 다른 함수 import 방법은??
        #     pass
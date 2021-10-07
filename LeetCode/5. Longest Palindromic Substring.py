class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_list = list(s)
        length = len(s_list)

        # 문자열 길이가 1 or 2 인 경우 먼저 처리
        if length == 1:
            return s
        elif length == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]

        else:
            # palindrome 체크해서 담을 리스트
            result = []

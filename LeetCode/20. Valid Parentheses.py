class Solution:
    def isValid(self, s: str) -> bool:
        s_list = list(s)
        check = []
        open_char = ['(', '{', '[']
        close_char = [')', '}', ']']
        for str in s_list:
            if str in open_char:
                check.append(str)
            if str in close_char:
                # check 리스트에 open_char 가 없는 경우
                if not check:
                    return False

                # 열린 기호와 매칭 가능하면 그대로 진행 / 아닐 경우 False
                if str == close_char[0]:
                   if check.pop() == open_char[0]:
                       pass
                   else:
                       return False
                elif str == close_char[1]:
                   if check.pop() == open_char[1]:
                       pass
                   else:
                       return False
                elif str == close_char[2]:
                   if check.pop() == open_char[2]:
                       pass
                   else:
                       return False

        # check 리스트가 비어 있어야 True
        if check:
            return False
        else:
            return True

result = Solution()
print(result.isValid(']'))

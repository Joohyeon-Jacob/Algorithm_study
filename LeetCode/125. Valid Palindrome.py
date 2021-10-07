class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 공백 제거 & 소문자로 변환 -> 각 글자를 리스트 원소로 하는 리스트 생성
        s = s.replace(' ','')
        s = s.lower()
        s_list = list(s)
        # 팰린드롬 여부 판단
        flag = True

        # s_list의 앞 글자 : a, 뒷 글자 : b
        a = 0
        b = len(s_list)-1
        # index 일치할때까지 순회
        while b-a >= 1:
            # 0~9 : ord --> 48~57
            # a~z : ord --> 97~122

            # 앞에서 & 뒤에서부터 순회
            # 문자가 다를 경우
            if s_list[a] != s_list[b]:
                # 앞 문자는 알파벳 or 숫자
                if (ord(s_list[a]) in range(48, 58)) or (ord(s_list[a]) in range(97, 123)):
                    # 뒷 문자는 알파벳도 아니고, 숫자도 아님
                    if (ord(s_list[b]) not in range(48, 58)) and (ord(s_list[b]) not in range(97, 123)):
                        b -= 1
                    else:
                        flag = False
                        break
                # 뒷 문자는 알파벳 or 숫자
                elif (ord(s_list[b]) in range(48, 58)) or (ord(s_list[b]) in range(97, 123)):
                    # 앞 문자는 알파벳도 아니고, 숫자도 아님
                    if (ord(s_list[a]) not in range(48, 58)) and (ord(s_list[a]) not in range(97, 123)):
                        a += 1
                    else:
                        flag = False
                        break
                # 두 문자 모두 알파벳도 아니고, 숫자도 아닌 경우
                elif (ord(s_list[a]) not in range(48, 58)) and (ord(s_list[a]) not in range(97, 123)) and (ord(s_list[b]) not in range(48, 58)) and (ord(s_list[b]) not in range(97, 123)):
                    a += 1
                    b -= 1

            # 문자가 같을 경우
            else:
                a += 1
                b -= 1
        return flag
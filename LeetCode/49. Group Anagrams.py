from typing import List

class Solution:
    def check_anagrams(self, target_str, check_str):
        # target_str 이 정해져 있을때, 주어진 check_str이 target_str의 anagram 중 하나인지 체크
        target_str_list = list(target_str)
        check_str_list = list(check_str)

        target_str_list.sort()
        check_str_list.sort()

        # sorting 한 결과를 비교
        if check_str_list == target_str_list:
            return True

        else:
            return False


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 단어 조합 담을 dict -> key(단어) : value(조합 가능한 anagram 담은 list)
        Anagrams_dict = {}

        for word in strs:

            flag = False
            # solution = Solution()
            for key in Anagrams_dict.keys():
                # anagram 조건 통과 -> Anagram_dict에 key: value 관계로 추가
                if self.check_anagrams(target_str=key, check_str=word):
                    Anagrams_dict[key].append(word)
                    flag = True

            if not flag:
                Anagrams_dict[word] = [word]

        result = []
        for anagrams in Anagrams_dict.values():
            result.append(anagrams)

        return result
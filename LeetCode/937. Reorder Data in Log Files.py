from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # digit-logs 담을 List
        digit_logs_list = []

        # Letter-logs 담을 List
        letter_logs_list = []

        for word in logs:
            # 두 번째 단어가 digit 인 경우
            if word.split()[1].isdigit():
                digit_logs_list.append(word)
            else:
                letter_logs_list.append(word)

        # 두 개의 키를 람다 표현식으로 정렬
        # (x.split()[1:] sort한 기준으롷 (x.split()[0] 을 정렬
        letter_logs_list.sort(key=lambda x: (x.split()[1:], x.split()[0]))

        # Letter-logs 뒤에 digit-logs 배치
        return letter_logs_list + digit_logs_list
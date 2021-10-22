from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1

'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # list2 순회하면서 list1 의 원소 필요한 위치에 추가

        # list2 원소가 추가된 위치(index 표시)
        added_point = 0

        length2 = len(list2)
        length1 = len(list1)

        while list2:
            num2 = list2.pop(0)
            # list 1 원소 순회하면서 비교
            for i in range(added_point, length1):
                if num2 > list1[i]:
                    # num이 list1의 마지막 원소일 경우
                    if i == length1 - 1:
                        # num2 와 list2 전체를 add
                        list1.append(num2)
                        list1 += list2
                        return list1

                    else:
                        continue

                # num2 <= list1[i]
                else:
                    list1.insert(i, num2)
                    # num2가 추가된 위치(index 표시)
                    added_point = i
                    length1 += 1
                    break

        return list1
'''

result = Solution()
print(result.mergeTwoLists([1,2,4], [1,3,4]))

#https://leetcode.com/problems/split-linked-list-in-parts/description/
# Definition for singly-linked list
from typing import Optional, List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def splitListToParts(self, ll, k: int) -> List[Optional[ListNode]]:
        head = Solution._constructLL(ll)
        slow, fast = head, head
        result = [[]]
        total_elements = 0
        while fast:
            fast, counter = Solution._moveKSteps(fast, k)
            result[0].append(slow.val)
            slow = slow.next
            if counter == k and fast is not None:
                total_elements += k
            else:
                total_elements += counter
                break
        qotient = (total_elements) // (k)
        remaintder = total_elements % k - 1
        for part in range(1,k):
            temp = []
            if qotient > 0:
                for _ in range(qotient):
                    temp.append(slow.val)
                    slow = slow.next
            if remaintder > 0:

                temp.append(slow.val)
                slow = slow.next
                remaintder -= 1
            result.append(temp)
        return result
    
    @staticmethod
    def _moveKSteps(fast, counter):
        for i in range(1, counter + 1):
            fast = fast.next
            if not fast:
                break
        return [fast, i]

    @staticmethod   
    def _constructLL(ll):
        current, head = None, None
        for item in ll:
            node = ListNode(item)
            if not head:
                head = node
                current = node
                continue
            current.next= node
            current = current.next
        return head
        

assert Solution().splitListToParts([1,2,3], k = 5) == [[1],[2],[3],[],[]]
assert Solution().splitListToParts([1,2,3,4,5,6,7,8,9,10], k = 3) == [[1,2,3,4],[5,6,7],[8,9,10]]
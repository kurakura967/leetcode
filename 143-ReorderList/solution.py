from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# problems that could not be answered correctly
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next  #3
        prev = slow.next = None
        while second:
            tmp = second.next  #4
            second.next = prev  # List(3, next=None) ->  List(4, next=3)
            prev = second  # prev = 3 -> List(4, next=3)
            second = tmp  # second = 4

        first, second = head, prev #first=ListNode(1, next=2)
        while second: # List(val=4, next=3)
            tmp1, tmp2 = first.next, second.next # 2, 3 -> 3, None
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2


if __name__ == '__main__':
    print(Solution().reorderList(ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3, next=ListNode(val=4)))))) # [1,4,2,3]

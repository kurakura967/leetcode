from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # first solution(runtime: 45 ms, memory: 17.72 MB)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        current = head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev


if __name__ == '__main__':
    print(Solution().reverseList(ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3, next=ListNode(val=4, next=ListNode(val=5)))))))  # [5,4,3,2,1]

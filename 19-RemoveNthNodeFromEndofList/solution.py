from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # first solution(runtime: 30 ms, memory: 16.59 MB)
    def removeNthFromEnd1(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # reverse the linked list
        prev = None
        current = head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next

        # remove the nth node from the end
        head = prev
        current = head
        prev = None
        cnt = 1
        while current:
            if cnt == n:
                current = current.next
                cnt += 1
                continue
            next = current.next
            current.next = prev
            prev = current
            current = next
            cnt += 1

        return prev

    # second solution(runtime: 37 ms, memory: 16.55 MB)
    def removeNthFromEnd2(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0 and right:
            right = right.next
            n -= 1
        # right = ListNode(3, next=ListNode(4))

        while right:

            left = left.next
            right = right.next
        # left = ListNode(2, next=ListNode(3, next=ListNode(4)))

        left.next = left.next.next
        # left = ListNode(2, next=ListNode(4))
        return dummy.next


if __name__ == '__main__':
    nodes = Solution().removeNthFromEnd2(ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3, next=ListNode(val=4)))), 2)  # [1,2,4]
    # while nodes:
    #     print(nodes.val)
    #     nodes = nodes.next

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    # problems that could not be answered correctly
    # first solution(runtime: 54ms, memory: 19.12MB)
    def hasCycle1(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next # ListNode(x=2, ...) -> ListNode(x=0, ...) -> ListNode(x=-4, ...)
            fast = fast.next.next # ListNode(x=0, ...) -> ListNode(x=2, ...) -> ListNode(x=-4, ...)
            if slow == fast:
                return True
        return False

    # second solution(runtime: 45ms, memory: 19.46MB)
    def hasCycle2(self, head: Optional[ListNode]) -> bool:
        hash_map = set()
        cur = head
        while cur:
            if cur in hash_map:
                return True
            hash_map.add(cur)
            cur = cur.next
        return False


if __name__ == '__main__':
    node = ListNode(x=3, next=ListNode(x=2, next=ListNode(x=0, next=ListNode(x=-4, next=ListNode(x=2, next=ListNode(0, next=ListNode(-4)))))))
    print(Solution().hasCycle1(node)) # True

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Problems that could not be answered correctly
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            k_th = self.getKth(group_prev, k)
            if not k_th:
                break
            group_next = k_th.next

            prev, curr = k_th.next, group_prev.next
            while curr != group_next:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            tmp = group_prev.next
            group_prev.next = k_th
            group_prev = tmp
        return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr


if __name__ == '__main__':
    print(Solution().reverseKGroup(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2)) # ListNode(2, ListNode(1, ListNode(4, ListNode(3, ListNode(5)))))

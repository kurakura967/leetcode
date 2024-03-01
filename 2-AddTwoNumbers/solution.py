from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # first solution(runtime: 56ms, memory: 16.60 MB)
    def addTwoNumbers1(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        current = None
        current_l1 = l1
        current_l2 = l2

        carry = 0

        while current_l1 or current_l2 or carry:

            val1 = current_l1.val if current_l1 else 0
            val2 = current_l2.val if current_l2 else 0

            sum = val1 + val2 + carry
            carry = sum // 10

            new_node = ListNode(sum % 10)

            if head is None:
                head = new_node
                current = head
            else:
                current.next = new_node
                current = current.next

            current_l1 = current_l1.next if current_l1 else None
            current_l2 = current_l2.next if current_l2 else None

        return head

    # second solution(runtime: 55ms, memory: 16.65 MB)
    def addTwoNumbers2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            val = val1 + val2 + carry
            carry = val // 10

            current.next = ListNode(val % 10)
            current = current.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next


if __name__ == '__main__':
    print(Solution().addTwoNumbers1(ListNode(2, ListNode(4, ListNode(3))), ListNode(5, ListNode(6, ListNode(4))))) # 7 -> 0 -> 8

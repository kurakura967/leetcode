from typing import Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Problems that could not be answered correctly
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        current = head

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next

            else:
                current.next = list2
                list2 = list2.next

            current = current.next
        current.next = list1 or list2
        return head.next


if __name__ == '__main__':
    list1 = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=4)))
    list2 = ListNode(val=1, next=ListNode(val=3, next=ListNode(val=4)))

    ans = Solution().mergeTwoLists(list1, list2)  # [1,1,2,3,4,4]
    for node in iter(lambda: ans, None):
        ans = node.next
        print(node.val)

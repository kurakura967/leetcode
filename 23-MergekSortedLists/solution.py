from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Problems that could not be answered correctly
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:

            merged_lists = []

            for i in range(0, len(lists), 2):
                print(i)
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                merged_lists.append(self.mergeList(l1, l2))

            lists = merged_lists
        return lists[0]

    def mergeList(self, l1, l2):
        print(l2)
        dummy = ListNode()
        tail = dummy

        while l1 and l2:

            # l1の値がl2の値より小さい場合はl1をtail.nextに設定し、l1を次のノードに進める
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next

            tail = tail.next

        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next


if __name__ == '__main__':
    print(Solution().mergeKLists([ListNode(1, ListNode(4, ListNode(5))), ListNode(1, ListNode(3, ListNode(4))), ListNode(2, ListNode(6))])) # ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4, ListNode(5, ListNode(6))))))))

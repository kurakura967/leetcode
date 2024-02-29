from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    # Problem that could not be answered correctly
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_copy = {None: None}

        cur = head
        while cur:
            copy = Node(cur.val)
            print("hoge")
            old_to_copy[cur] = copy
            cur = cur.next

        # old_to_copy = {Node(x=7, next=Node(x=13, next=Node(x=11, next=Node(x=10, next=Node(x=1)))), random=....): Node(x=7, next=None, random=None),}
        cur = head
        while cur:
            copy = old_to_copy[cur] # copy = Node(x=7, next=None, random=None)
            copy.next = old_to_copy[cur.next] # copy.next = Node(x=13, next=None, random=None)
            copy.random = old_to_copy[cur.random] # copy.random = None
            cur = cur.next

        return old_to_copy[head]


if __name__ == '__main__':
    print(Solution().copyRandomList(Node(x=7, next=Node(x=13, next=Node(x=11, next=Node(x=10, next=Node(x=1)))), random=Node())))  # 7 -> 13 -> 11 -> 10 -> 1

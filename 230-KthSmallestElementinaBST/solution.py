from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Problem that could not be answered correctly
    def kthSmallest1(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def dfs(root):
            if not root:
                return

            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        dfs(root)
        return res[k-1]

    def kthSmallest2(self, root: Optional[TreeNode], k: int) -> int:

        n = 0
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val
            cur = cur.right


if __name__ == '__main__':
    print(Solution().kthSmallest2(root=TreeNode(val=3, left=TreeNode(val=1, right=TreeNode(val=2)), right=TreeNode(val=4)), k=1))

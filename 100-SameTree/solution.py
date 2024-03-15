from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # first solution(runtime: 43 ms, memory: 16.54 MB)
    def isSameTree1(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(p, q):

            if not p or not q:
                return p == q

            if p.val != q.val:
                return False

            return dfs(p.left, q.left) and dfs(p.right, q.right)

        return dfs(p, q)

    # second solution(runtime: 29 ms, memory: 16.52MB)
    def isSameTree2(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p and not q:
            return True

        if not p or not q or p.val != q.val:
            return False

        return self.isSameTree2(p.left, q.left) and self.isSameTree2(p.right, q.right)


if __name__ == '__main__':
    print(Solution().isSameTree1(TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(1, TreeNode(2), TreeNode(3)))) # True

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Problems that could not be answered correctly
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        res = [0]

        def dfs(root):
            if not root:
                return -1

            left = dfs(root.left)
            right = dfs(root.right)
            res[0] = max(res[0], 2 + left + right)
            return 1 + max(left, right)

        dfs(root)
        return res[0]


if __name__ == '__main__':
    print(Solution().diameterOfBinaryTree(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))) == 3)

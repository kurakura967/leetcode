from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Problem that could not be answered correctly
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        res = []

        def dfs(root, depth):
            if not root:
                return
            if depth == len(res):
                res.append(root.val)
            dfs(root.right, depth + 1)
            dfs(root.left, depth + 1)

        dfs(root, 0)
        return res


if __name__ == '__main__':
    print(Solution().rightSideView(root=TreeNode(val=1, left=TreeNode(val=2, right=TreeNode(val=5)), right=TreeNode(val=3, right=TreeNode(val=4)))))

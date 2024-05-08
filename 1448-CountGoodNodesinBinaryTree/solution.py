# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Problem that could not be answered correctly
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        def dfs(root, max_value):
            if root is None:
                return 0

            ans = 1 if root.val >= max_value else 0
            max_value = max(root.val, max_value)
            ans += dfs(root.left, max_value)
            ans += dfs(root.right, max_value)
            return ans

        return dfs(root, root.val)


if __name__ == '__main__':
    print(Solution().goodNodes(root=TreeNode(val=3, left=TreeNode(val=1, left=TreeNode(val=3)), right=TreeNode(val=4, left=TreeNode(val=1), right=TreeNode(val=5)))) == 4)

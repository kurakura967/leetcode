from typing import Optional

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def valid(node, left, right):
            if not node:
                return True

            if not (node.val < right and node.val > left):
                print(node.val)
                print(right)
                print(left)
                return False

            return (valid(node.left, left, node.val) and valid(node.right, node.val, right))

        return valid(root, float("-inf"), float("inf"))

if __name__ == '__main__':
    #print(Solution().isValidBST(root=TreeNode(val=2, left=TreeNode(val=1), right=TreeNode(val=3))))
    #print(Solution().isValidBST(root=TreeNode(val=5, left=TreeNode(val=1), right=TreeNode(val=4, left=TreeNode(val=3), right=TreeNode(val=6)))))
    print(Solution().isValidBST(root=TreeNode(val=5, left=TreeNode(val=4), right=TreeNode(val=6, left=TreeNode(val=3), right=TreeNode(val=7)))))


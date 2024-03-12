from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Problems that could not be answered correctly
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


    def maxDepth2(self, root: Optional[TreeNode]) -> int:

        stack = [[root, 1]]
        res = 0

        while stack:
            node, depth = stack.pop()  # node=root, depth=1, stack=[] ->  node=right, depth=2, stack=[[left, 2]] -> node=right, depth=3, stack=[[left, 2], [left, 3]]

            if node:
                res = max(res, depth) # res=1 -> res=2 -> res=3
                stack.append([node.left, depth + 1]) # stack=[[left, 2]] -> stack=[[left, 2], [left, 3]] -> stack=[[left, 2], [left, 3], [None, 4]]
                stack.append([node.right, depth + 1]) # stack=[[left, 2], [right, 2]] -> stack=[[left, 2], [left, 3], [right, 3]] -> stack=[[left, 2], [left, 3], [None, 4], [None, 4]]
        return res



if __name__ == '__main__':
    print(Solution().maxDepth(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))))) # 3

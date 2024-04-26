from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # first solution(runtime: 42 ms, memory: 17.43 MB)
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:

        if not root:
            return []
        result = []
        queue = [root]

        while queue:
            level = []
            level_size = len(queue)
            for _ in range(level_size):
                print(level_size)
                node = queue.pop(0)
                level.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.append(level)

        return result


if __name__ == '__main__':
    node = TreeNode(val=3, left=TreeNode(val=9), right=TreeNode(val=20, left=TreeNode(val=15), right=TreeNode(val=7)))
    print(Solution().levelOrder(node) == [[3],[9,20],[15,7]])

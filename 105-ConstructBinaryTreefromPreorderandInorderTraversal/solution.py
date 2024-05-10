from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Problem that could not be answered correctly
class Solution:
    def buildTree1(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:

        if not preorder or not inorder:
            return None

        # root value of preorder
        preorder_value = preorder[0]
        Tree = TreeNode(preorder_value)
        inorder_root_index = inorder.index(preorder_value)

        Tree.left = self.buildTree1(preorder[1:inorder_root_index+1], inorder[:inorder_root_index])
        Tree.right = self.buildTree1(preorder[inorder_root_index+1:], inorder[inorder_root_index+1:])

        return Tree

    def buildTree2(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:

        if inorder:

            preorder_value = preorder.pop(0)
            ind = inorder.index(preorder_value)
            Tree = TreeNode(inorder[ind])
            Tree.left = self.buildTree2(preorder, inorder[0:ind])
            Tree.right = self.buildTree2(preorder, inorder[ind+1:])

            return Tree


if __name__ == '__main__':
    res = Solution().buildTree2(preorder = [3,9,20,15,7], inorder = [9,3,15,20,7])


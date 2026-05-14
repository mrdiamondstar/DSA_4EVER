# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#DFS
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def bst(node):
            if not node:
                return 0

            left=bst(node.left)
            if left == -1:
                return -1

            right=bst(node.right)
            if right == -1:
                return -1
            
            if left == -1 or right == -1:
                return -1

            if abs(left-right) > 1:
               return -1
     
            return 1 + max(left, right) 

        return bst(root) != -1



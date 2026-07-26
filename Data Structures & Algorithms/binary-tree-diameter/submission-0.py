# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res=0
        def computeHeight(root:Optional[TreeNode]):
            nonlocal res
            if root is None:
                return 0
            left_h = computeHeight(root.left)
            right_h = computeHeight(root.right)
            res = max(res,left_h+right_h)
            return 1 + max(left_h,right_h)
        computeHeight(root)
        return res

        
        
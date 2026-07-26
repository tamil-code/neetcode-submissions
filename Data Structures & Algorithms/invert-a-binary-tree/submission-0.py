# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def swapNode(node:Optional[TreeNode]) -> None:
            if not node:
                return None
            temp = node.left
            node.left = node.right
            node.right = temp
            swapNode(node.left)
            swapNode(node.right)
        swapNode(root)
        return root
        
        
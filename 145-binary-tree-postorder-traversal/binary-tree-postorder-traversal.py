# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        pso=[]
        def po(root):
            if root is None:
                return
            po(root.left)
            po(root.right)
            pso.append(root.val)
        po(root)
        return pso
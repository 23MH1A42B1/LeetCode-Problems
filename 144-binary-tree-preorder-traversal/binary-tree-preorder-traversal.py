# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        pst=[]
        def postorder(root):
            if root is None:
                return
            pst.append(root.val)
            postorder(root.left)
            postorder(root.right)
        postorder(root)
        return pst
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, node: Optional[TreeNode]) -> List[int]:
        result = []

        def inorder(node):
            if node is None:
                return

            inorder(node.left)

            result.append(node.val)

            inorder(node.right)

        inorder(node)

        return result
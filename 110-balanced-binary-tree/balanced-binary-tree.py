# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node is None:
                return 0
            
            left_h = dfs(node.left)
            right_h = dfs(node.right)

            # Check if not balanced tree
            if (left_h == -1) or (right_h == -1):
                return -1
            elif abs(left_h - right_h) > 1:
                return -1
            else:
                return max(left_h, right_h) + 1
        return dfs(root) != -1
        
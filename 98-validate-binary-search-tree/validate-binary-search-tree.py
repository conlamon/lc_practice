# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.valid_dfs(root=root, min_val=float("-inf"), max_val=float("inf"))
    
    def valid_dfs(self, root: TreeNode, min_val: int, max_val: int):
        # Base case
        if root is None:
            return True
        
        # Check if not valid and return
        if not (min_val < root.val < max_val):
            return False
        
        # Recurse left
        left_val = self.valid_dfs(root.left, min_val, root.val)
        # Recurse right
        right_val = self.valid_dfs(root.right, root.val, max_val)

        return left_val and right_val

        
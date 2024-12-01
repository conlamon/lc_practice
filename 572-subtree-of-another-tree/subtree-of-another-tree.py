# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Use two functions, one as driver function to iterate down the tree S
        # The other checks if tree T is the same starting at node S
        # Perform a pre-order traversal on tree
        # Base cases for both t and s
        def is_subtree_dfs(s, t) -> bool:
            # Base cases:
            if not t:
                return True
            if not s:
                return False
            
            # Pre-order check node value is subtree
            if is_subtree(s, t):
                return True
            # Recurse down both trees and only one side needs to be true 
            return is_subtree_dfs(s.left, t) or is_subtree_dfs(s.right, t)
        
        def is_subtree(s, t) -> bool:
            # Base cases
            # First check if both null
            if not s and not t:
                return True
            # if not both null, but one is null return False
            if s and t and s.val == t.val:
                return is_subtree(s.left, t.left) and is_subtree(s.right, t.right)
            return False

        if not root:
            return False
        else:
            return is_subtree_dfs(root, subRoot)
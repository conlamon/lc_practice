# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_val):
            # Preorder traversal 
            # Return total count of good nodes
            # Pass state of max val seen so far
            # Base case:
            if node is None:
                return 0
            
            if node.val >= max_val:
                # Node is good
                res = 1
            else:
                # node is not good
                res = 0
            # Update max val
            max_val = max(max_val, node.val)
            # Recurse and sum up total good nodes
            res += dfs(node.left, max_val)
            res += dfs(node.right, max_val)
            return res
        # Call function
        return dfs(root, root.val)
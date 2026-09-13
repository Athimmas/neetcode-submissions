# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root:
                return [True,0]

            LBalance,LHeight = dfs(root.left)
            RBalance,RHeight = dfs(root.right)

            Balanced = abs(LHeight - RHeight) <= 1

            return (Balanced and LBalance and RBalance,max(LHeight,RHeight) + 1)

        res,temp = dfs(root)
        return res
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val

        def dfs(root):
            nonlocal res
            
            if not root:
                return 0

            MaxLeft = max(dfs(root.left),0)
            MaxRight = max(dfs(root.right),0)

            cursum = MaxLeft + MaxRight + root.val
            res = max(cursum,res)

            return root.val + max(MaxLeft,MaxRight)

        dfs(root)
        return res
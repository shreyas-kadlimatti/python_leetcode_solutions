# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res=[]
        self.inord(root,res,k)
        return res[-1]

    def inord(self,root,res,k):
        if root is None:
            return 
        self.inord(root.left,res,k)
        if k==len(res):
            res
        else:
            res.append(root.val)
        self.inord(root.right,res,k)
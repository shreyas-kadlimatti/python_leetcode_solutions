# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        lvl=0
        self.rightview(root,lvl,res)
        return res

    def rightview(self,root,lvl,res):
        if root is None:
            return
        if lvl==len(res):
            res.append(root.val)
        self.rightview(root.right,lvl+1,res)
        self.rightview(root.left,lvl+1,res)
        

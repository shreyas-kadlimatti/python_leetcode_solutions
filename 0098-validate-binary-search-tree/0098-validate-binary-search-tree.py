# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return False 

        self.prev=None 
        self.isvalid=True 
        self.inord(root)
        return self.isvalid


    def inord(self,cur):
        if cur is None:
            return 
        self.inord(cur.left)

        if self.prev is not None and self.prev>=cur.val:
          self.isvalid=False
          return 
        self.prev=cur.val
       
        self.inord(cur.right)
          
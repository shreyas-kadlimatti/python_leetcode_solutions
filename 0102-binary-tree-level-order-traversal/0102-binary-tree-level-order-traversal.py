# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q=deque([root,None])
        # q.append(root)
        # q.append(None)
        res=[]
        lvl=[]

        while q:
            cur=q.popleft()

            if cur is None:
                res.append(lvl)
                lvl=[]
                if q:
                    q.append(None)
                else:
                    break
            else:
                lvl.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
        return res

        
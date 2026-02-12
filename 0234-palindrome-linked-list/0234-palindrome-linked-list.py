# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # l=[]
        # cur=head 
        # while cur!=None:
        #     l.append(cur.val)
        #     cur=cur.next
        # if l==l[::-1]:
        #     return True
        # return False

        #base case:
        if not head or not head:
            return True
        
        #find middle of linklist
        slow,fast=head,head 

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next 
        
        #reversing second half of ll
        cur=slow 
        pre=None

        while cur:
            temp=cur.next
            cur.next=pre
            pre=cur
            cur=temp
            #finally pre will be pointing to head of reversed list 

        #comparing reversed first half with second half 
        first,second=head,pre 
        while second and first:
            if first.val!=second.val:
                return False
            first=first.next
            second=second.next 
        return True


        
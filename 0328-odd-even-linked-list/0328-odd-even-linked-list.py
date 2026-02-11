# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
            
        odd_head=head 
        op=odd_head
        even_head=head.next
        ep=even_head
        while op.next and ep.next :
            op.next=op.next.next
            op=op.next
            ep.next=ep.next.next
            ep=ep.next
        op.next=even_head 
        return odd_head
      

                
        
       
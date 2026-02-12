# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        len=0
        cur=head
        while cur:
            len+=1 
            cur=cur.next
        # print(c)
        # print(cur)
        for i in range(k%len):
            cur=head
            while cur.next and  cur.next.next:
                cur=cur.next

            temp=cur.next
            temp.next=head 
            cur.next=None
            head=temp
        return head

              


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head :
            return None
        
        tail = ListNode(head.val)
        
        while head.next :
            now = ListNode(head.next.val, tail)
            tail = now
            head = head.next
        
        return tail
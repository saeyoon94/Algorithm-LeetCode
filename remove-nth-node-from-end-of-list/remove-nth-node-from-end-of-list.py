# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        result = slow = head
        fast = head
        
        if not result.next :
            return None
        
        for _ in range(n) :
            fast = fast.next
            
        if not fast :
            return result.next
            
        while fast and fast.next :
            slow = slow.next
            fast = fast.next
            
        slow.next = slow.next.next
        
        
        return result
        
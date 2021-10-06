# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 :
            return l2
        elif not l2 :
            return l1
        
        
        p1 = l1
        p2 = l2
        cur = None
        if p1.val < p2.val :
            cur = p1
            p1 = p1.next
        else :
            cur = p2
            p2 = p2.next
        
        result = cur
        
        while p1 and p2 :
            if p1.val < p2.val :
                cur.next = p1
                cur = cur.next
                p1 = p1.next
            else :
                cur.next = p2
                cur = cur.next
                p2 = p2.next
                
        if p1 :
            cur.next = p1
        
        elif p2 :
            cur.next = p2
            
        return result
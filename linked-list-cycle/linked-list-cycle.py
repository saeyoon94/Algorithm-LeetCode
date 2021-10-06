# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head :
            return False
        
        hashset = set()
        hashset.add(head)
        
        while head.next :
            if head.next in hashset :
                return True
            else :
                hashset.add(head.next)
                head = head.next
                
        return False
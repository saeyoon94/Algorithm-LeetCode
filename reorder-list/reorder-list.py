# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        q = deque([])
        
        while head :
            q.append(head)
            head = head.next
            
        if len(q) <= 2 :
            return
            
        start = 1
        end = len(q) - 1
        cur = q[0]
      
        while start <= end :
            
            cur.next = q[end]
            cur = cur.next
            
            if start != end :
                cur.next = q[start]
                cur = cur.next

            start += 1
            end -= 1
            
        cur.next = None
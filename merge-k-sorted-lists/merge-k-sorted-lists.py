# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __lt__(self, other) :
        return self.val < other.val
        
class Solution:
    
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        class Wrapper:
            def __init__(self, node=None):
                self.val = node.val
                self.node = node

            def __lt__(self,other) :
                return self.val < other.val

        lists = [_list for _list in lists if _list]
        
        if not lists :
            return None
        
        n = len(lists)
        result = now = ListNode()
        heap = []
        
        for _list in lists :
            heapq.heappush(heap, Wrapper(_list))
        
        
        while heap :
            node = heapq.heappop(heap).node
            now.next = node
            now = node
            
            if node.next :
                heapq.heappush(heap, Wrapper(node.next))
        
        return result.next
            
        
        
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    
    def cloneGraph(self, node: 'Node') -> 'Node':
        visited = [None] * 101
        return self.clone(node, visited)
    
    def clone(self, node, visited) :
        if not node :
            return None
        cloned = Node(val = node.val)
        visited[cloned.val] = cloned
        if len(node.neighbors) > 0 :
            for neighbor in node.neighbors :
                if not visited[neighbor.val] :
                    cloned.neighbors.append(self.clone(neighbor, visited))
                else :
                    cloned.neighbors.append(visited[neighbor.val])
        
        return cloned
                
        
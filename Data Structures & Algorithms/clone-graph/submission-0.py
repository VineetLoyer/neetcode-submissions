"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}
        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            
            copy = Node(node.val)

            oldToNew[node] = copy # we create copy of current node and store it in oldToNew dict for future

            for n in node.neighbors:
                copy.neighbors.append(dfs(n)) #visit all neighbors of current node and run dfs 
            
            return copy
        
        return dfs(node) if node else None
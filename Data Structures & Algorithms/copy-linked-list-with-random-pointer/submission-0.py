"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = { None: None } #mapping every old node to a copy node

        cur = head #first pass
        while cur:
            copy = Node(cur.val)  #create clones of nodes.
            oldToCopy[cur] = copy #map old node to copy node
            cur = cur.next

        cur = head #second pass
        while cur:
            copy = oldToCopy[cur] 
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next

        return oldToCopy[head]





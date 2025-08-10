"""
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
"""
from collections import deque
class Solution:
    def levelOrder(root):
        # Your code here
        ans = []
        tmp = []
        curr_level = 0
        q = deque()
        q.append((root,0))
        while len(q)!=0:
            node,level = q.popleft()
            if curr_level == level:
                tmp.append(node.data)
                if node.left:
                    q.append((node.left,curr_level+1))
                if node.right:
                    q.append((node.right,curr_level+1))
            else:
                ans.append(tmp)
                tmp = [node.data]
                curr_level = level
                if node.left:
                    q.append((node.left,curr_level+1))
                if node.right:
                    q.append((node.right,curr_level+1))
        ans.append(tmp)
        return ans
from collections import deque
from typing import List,Optional

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def bfs_levelorder(self,root:Optional[TreeNode])->List[List[int]]:
        
        if not root:
            return []

        result=[]
        q=deque([root])
            
        while q:
            level=[]
            level_size=len(q)

            for _ in range(level_size):

                node2 = q.popleft()
                level.append(node2.val)  # append the node value to the level list   

                if node2.left:
                    q.append(node2.left)  # append the left child to the queue
                if node2.right:
                    q.append(node2.right)  # append the right child to the queue

            result.append(level)  # append the level list to the result list      

        return result
    

    def print_level(self,result):
            for level in result:    
                for node in level:
                    print(node, end=" ")
                print()
                
root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.left=TreeNode(4)
root.left.right=TreeNode(5)
root.right.left=TreeNode(6)
root.right.right=TreeNode(7)

obj=Solution()
result=obj.bfs_levelorder(root)
print(result)
obj.print_level(result)
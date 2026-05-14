from typing import List,Optional
class TreeNode:
    def __init__(self,val=0,left=None, right=0):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def all_dfs(self,root:Optional[TreeNode])->List[List[int]]:
        
        result=[]
        
        #PRE_ORDER DFS
        pre_order = []
        def preorder(root):
            if not root:
                return 
            
            pre_order.append(root.val)
            preorder(root.left)
            preorder(root.right)
        
        result.append(pre_order)

        #IN_ORDER DFS
        in_order=[]
        def inorder(root):
            if not root:
                return
            
            inorder(root.left)
            in_order.append(root.val)
            inorder(root.right)
        result.append(in_order)
          
        #POST_ORDER DFS   
        post_order=[]
        def postorder(root):
            if not root:
                return 
            
            postorder(root.left)
            postorder(root.right)
            post_order.append(root.val)

        result.append(post_order)
        
        #AFTER Defining funcions ,we should call all funcions here ,only main methos function all_dfs is called by creating object 
        #all other functions are called here.
        preorder(root)
        inorder(root)
        postorder(root)
        return result
root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.left=TreeNode(4)
root.left.right=TreeNode(5)
root.right.left=TreeNode(6)
root.right.right= TreeNode(7)

obj=Solution()

result=obj.all_dfs(root)
print(result)


            
            
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        self.st=[]
        self.count=0

        def dfs(node):
            if not node:
                return 
            if not self.st or  node.val>=max(self.st):
                self.count+=1
            self.st.append(node.val)    
            dfs(node.left)
            dfs(node.right)

            if self.st:self.st.pop()

        dfs(root)
        return self.count    

        
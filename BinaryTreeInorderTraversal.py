class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        result = []
        self.helper(root, result)
        return result
    
    def helper(self, node, result):
        if node is None:
            return
        self.helper(node.left, result)  
        result.append(node.val)         
        self.helper(node.right, result) 


root1 = TreeNode(1, None, TreeNode(2, TreeNode(3)))

obj = Solution()
print(obj.inorderTraversal(root1))  

root2 = TreeNode(1,
    TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(6), TreeNode(7))),
    TreeNode(3, None, TreeNode(8, TreeNode(9)))
)
print(obj.inorderTraversal(root2))  


print(obj.inorderTraversal(None))   


root4 = TreeNode(1)
print(obj.inorderTraversal(root4))  

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        return self.DFS(root, sum)
        
    def DFS(self, root, sum):
        if not root:
            return False
        if not root.left and not root.right and sum == root.val:
            return True
        return self.DFS(root.left, sum - root.val) or self.DFS(root.right, sum - root.val)

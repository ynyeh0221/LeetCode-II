# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        p = root
        self.helper(p)
        return root
        
    def helper(self, root):
        if not root:
            return []
        temp = root.left
        root.left = root.right
        root.right = temp
        self.helper(root.left)
        self.helper(root.right)

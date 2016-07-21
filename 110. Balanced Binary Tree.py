# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return True if self.helper(root) >= 0 else False
    
    def helper(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        l = self.helper(root.left)
        r = self.helper(root.right)
        if l >= 0 and r >= 0:
            if abs(l-r) > 1:
                return -1
            return max(l, r) + 1

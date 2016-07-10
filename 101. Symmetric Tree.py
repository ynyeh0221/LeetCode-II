# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        p = root.left
        q = root.right
        return self.helper(p, q)
    
    def helper(self, p, q):
        if not p and not q:
            return True
        if (not p and q) or (not q and p):
            return False
        if p.val != q.val:
            return False
        return self.helper(p.left, q.right) and self.helper(p.right, q.left)
